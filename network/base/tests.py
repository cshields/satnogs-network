import random
from datetime import timedelta

import factory
from factory import fuzzy
from django.utils.timezone import now

from network.base.models import (ANTENNA_BANDS, ANTENNA_TYPES, Mode, Antenna,
                                 Satellite, Station, Transmitter, Observation)
from network.users.tests import UserFactory


class ModeFactory(factory.django.DjangoModelFactory):
    """Antenna model factory."""
    name = fuzzy.FuzzyText()

    class Meta:
        model = Mode


class AntennaFactory(factory.django.DjangoModelFactory):
    """Antenna model factory."""
    frequency = fuzzy.FuzzyFloat(200, 500)
    band = fuzzy.FuzzyChoice(choices=ANTENNA_BANDS)
    antenna_type = fuzzy.FuzzyChoice(choices=ANTENNA_TYPES)

    class Meta:
        model = Antenna


class StationFactory(factory.django.DjangoModelFactory):
    """Station model factory."""
    owner = factory.SubFactory(UserFactory)
    name = fuzzy.FuzzyText()
    image = factory.django.ImageField()
    alt = fuzzy.FuzzyInteger(0, 800)
    lat = fuzzy.FuzzyFloat(-20, 70)
    lng = fuzzy.FuzzyFloat(-180, 180)
    featured_date = fuzzy.FuzzyDateTime(now() - timedelta(days=10), now())
    active = fuzzy.FuzzyChoice(choices=[True, False])
    last_seen = fuzzy.FuzzyDateTime(now() - timedelta(days=10), now())

    @factory.post_generation
    def antennas(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for antenna in extracted:
                if random.randint(0, 1):
                    self.antenna.add(antenna)

    class Meta:
        model = Station


class SatelliteFactory(factory.django.DjangoModelFactory):
    """Sattelite model factory."""
    norad_cat_id = fuzzy.FuzzyInteger(2000, 4000)
    name = fuzzy.FuzzyText()

    class Meta:
        model = Satellite


class TransmitterFactory(factory.django.DjangoModelFactory):
    """Transmitter model factory."""
    description = fuzzy.FuzzyText()
    alive = fuzzy.FuzzyChoice(choices=[True, False])
    uplink_low = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    uplink_high = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    downlink_low = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    downlink_high = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    mode = factory.SubFactory(ModeFactory)
    invert = fuzzy.FuzzyChoice(choices=[True, False])
    baud = fuzzy.FuzzyInteger(4000, 22000, step=1000)
    satellite = factory.SubFactory(SatelliteFactory)

    class Meta:
        model = Transmitter


class ObservationFactory(factory.django.DjangoModelFactory):
    """Observation model factory."""
    satellite = factory.SubFactory(SatelliteFactory)
    author = factory.SubFactory(UserFactory)
    start = fuzzy.FuzzyDateTime(now() - timedelta(days=3),
                                now() + timedelta(days=3))
    end = factory.LazyAttribute(
        lambda x: x.start + timedelta(hours=random.randint(1, 8))
    )
    transmitter = factory.Iterator(Transmitter.objects.all())

    class Meta:
        model = Observation
