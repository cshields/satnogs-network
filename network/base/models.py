from datetime import datetime, timedelta
from shortuuidfield import ShortUUIDField

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.utils.html import format_html

from network.users.models import User


ANTENNA_BANDS = ['HF', 'VHF', 'UHF', 'L', 'S', 'C', 'X', 'KU']
ANTENNA_TYPES = (
    ('dipole', 'Dipole'),
    ('yagi', 'Yagi'),
    ('helical', 'Helical'),
    ('parabolic', 'Parabolic'),
    ('vertical', 'Verical'),
)


class Mode(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.name


class Antenna(models.Model):
    """Model for antennas tracked with SatNOGS."""
    frequency = models.FloatField(validators=[MinValueValidator(0)])
    band = models.CharField(choices=zip(ANTENNA_BANDS, ANTENNA_BANDS),
                            max_length=5)
    antenna_type = models.CharField(choices=ANTENNA_TYPES, max_length=15)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.band, self.antenna_type, self.frequency)


class Station(models.Model):
    """Model for SatNOGS ground stations."""
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='ground_stations', blank=True)
    alt = models.PositiveIntegerField(help_text='In meters above ground')
    lat = models.FloatField(validators=[MaxValueValidator(90),
                                        MinValueValidator(-90)])
    lng = models.FloatField(validators=[MaxValueValidator(180),
                                        MinValueValidator(-180)])
    qthlocator = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    antenna = models.ManyToManyField(Antenna, blank=True,
                                     help_text=('If you want to add a new Antenna '
                                                'contact SatNOGS Team'))
    featured_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-active', '-last_seen']

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return settings.STATION_DEFAULT_IMAGE

    @property
    def online(self):
        try:
            heartbeat = self.last_seen + timedelta(minutes=int(settings.STATION_HEARTBEAT_TIME))
            return self.active and heartbeat > now()
        except:
            return False

    def state(self):
        if self.online:
            return format_html('<span style="color:green">Online</span>')
        else:
            return format_html('<span style="color:red">Offline</span>')

    @property
    def success_rate(self):
        observations = self.data_set.all().count()
        success = self.data_set.exclude(payload='').count()
        if observations:
            return int(100 * (float(success) / float(observations)))
        else:
            return False

    def __unicode__(self):
        return "%d - %s" % (self.pk, self.name)


class Satellite(models.Model):
    """Model for SatNOGS satellites."""
    norad_cat_id = models.PositiveIntegerField()
    name = models.CharField(max_length=45)
    names = models.TextField(blank=True)
    image = models.ImageField(upload_to='satellites', blank=True)

    class Meta:
        ordering = ['norad_cat_id']

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return settings.SATELLITE_DEFAULT_IMAGE

    @property
    def latest_tle(self):
        try:
            latest_tle = Tle.objects.filter(satellite=self).latest('updated')
            return latest_tle
        except Tle.DoesNotExist:
            return False

    @property
    def tle_no(self):
        try:
            line = self.latest_tle.tle1
            return line[65:68]
        except:
            return False

    @property
    def tle_epoch(self):
        try:
            line = self.latest_tle.tle1
            yd, s = line[18:32].split('.')
            epoch = (datetime.strptime(yd, "%y%j") +
                     timedelta(seconds=float("." + s) * 24 * 60 * 60))
            return epoch
        except:
            return False

    def __unicode__(self):
        return self.name


class Tle(models.Model):
    tle0 = models.CharField(max_length=100, blank=True)
    tle1 = models.CharField(max_length=200, blank=True)
    tle2 = models.CharField(max_length=200, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    satellite = models.ForeignKey(Satellite, related_name='tles', null=True)

    class Meta:
        ordering = ['tle0']

    def __unicode__(self):
        return self.tle0


class Transmitter(models.Model):
    """Model for antennas transponders."""
    uuid = ShortUUIDField(db_index=True)
    description = models.TextField()
    alive = models.BooleanField(default=True)
    uplink_low = models.PositiveIntegerField(blank=True, null=True)
    uplink_high = models.PositiveIntegerField(blank=True, null=True)
    downlink_low = models.PositiveIntegerField(blank=True, null=True)
    downlink_high = models.PositiveIntegerField(blank=True, null=True)
    mode = models.ForeignKey(Mode, related_name='transmitters', blank=True,
                             null=True, on_delete=models.SET_NULL)
    invert = models.BooleanField(default=False)
    baud = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    satellite = models.ForeignKey(Satellite, related_name='transmitters', null=True)

    def __unicode__(self):
        return self.description


class Observation(models.Model):
    """Model for SatNOGS observations."""
    satellite = models.ForeignKey(Satellite)
    transmitter = models.ForeignKey(Transmitter, null=True, related_name='observations')
    tle = models.ForeignKey(Tle, null=True)
    author = models.ForeignKey(User)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ['-start', '-end']

    @property
    def is_past(self):
        return self.end < now()

    @property
    def is_future(self):
        return self.end > now()

    @property
    def is_deletable(self):
        deletion = self.start - timedelta(minutes=int(settings.OBSERVATION_MAX_DELETION_RANGE))
        return deletion > now()

    @property
    def has_data(self):
        return self.data_set.exclude(payload='').count()

    def __unicode__(self):
        return "%d" % self.id


class Data(models.Model):
    """Model for observation data."""
    start = models.DateTimeField()
    end = models.DateTimeField()
    observation = models.ForeignKey(Observation)
    ground_station = models.ForeignKey(Station)
    payload = models.FileField(upload_to='data_payloads', blank=True, null=True)

    @property
    def is_past(self):
        return self.end < now()

    class Meta:
        ordering = ['-start', '-end']
