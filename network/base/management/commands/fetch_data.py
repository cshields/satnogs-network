import json
import urllib2

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from network.base.models import Satellite, Transmitter


class Command(BaseCommand):
    help = 'Provide DB API endpoint'

    def handle(self, *args, **options):
        apiurl = settings.DB_API_ENDPOINT
        satellites_url = "{0}satellites".format(apiurl)
        transmitters_url = "{0}transmitters".format(apiurl)
        self.stdout.write("Fetching from: {0}".format(satellites_url))
        try:
            satellites = urllib2.urlopen(satellites_url).read()
            transmitters = urllib2.urlopen(transmitters_url).read()
        except:
            raise CommandError('API is unreachable')

        for satellite in json.loads(satellites):
            norad_cat_id = satellite['norad_cat_id']
            name = satellite['name']
            try:
                sat = Satellite.objects.get(norad_cat_id=norad_cat_id)
                self.stdout.write('Satellite {0}-{1} already exists'.format(norad_cat_id, name))
            except:
                sat = Satellite(norad_cat_id=norad_cat_id, name=name)
                sat.save()
                self.stdout.write('Satellite {0}-{1} added'.format(norad_cat_id, name))

        for transmitter in json.loads(transmitters):
            norad_cat_id = transmitter['norad_cat_id']
            uuid = transmitter['uuid']
            description = transmitter['description']

            try:
                sat = Satellite.objects.get(norad_cat_id=norad_cat_id)
            except:
                self.stdout.write('Satellite {0} not present'.format(norad_cat_id))
            transmitter.pop('norad_cat_id')
            try:
                existing_transmitter = Transmitter.objects.get(uuid=uuid)
                existing_transmitter.__dict__.update(transmitter)
                existing_transmitter.satellite = sat
                self.stdout.write('Transmitter {0}-{1} updated'.format(uuid, description))
            except Transmitter.DoesNotExist:
                new_transmitter = Transmitter.objects.create(**transmitter)
                new_transmitter.satellite = sat
                new_transmitter.save()
                self.stdout.write('Transmitter {0}-{1} created'.format(uuid, description))
