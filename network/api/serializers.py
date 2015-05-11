from django.conf import settings
from django.contrib.sites.models import Site
from rest_framework import serializers

from network.base.models import (Antenna, Data, Observation, Satellite,
                                 Station, Transponder)


class AntennaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antenna
        fields = ('frequency', 'band', 'antenna_type')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('owner', 'name', 'image', 'alt', 'lat', 'lng',
                  'antenna', 'featured_date', 'id')

    image = serializers.SerializerMethodField('image_url')

    def image_url(self, obj):
        site = Site.objects.get_current()
        return '{}{}{}'.format(site, settings.MEDIA_URL, obj.image)


class SatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = ('norad_cat_id', 'name')


class TransponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transponder
        fields = ('description', 'alive', 'uplink_low', 'uplink_high',
                  'downlink_low', 'downlink_high', 'mode', 'invert',
                  'baud', 'satellite')


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('satellite', 'transponder', 'author', 'start', 'end')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'observation', 'ground_station', 'payload')
        read_only_fields = ['id', 'start', 'end', 'observation', 'ground_station']


class JobSerializer(serializers.ModelSerializer):
    frequency = serializers.SerializerMethodField()
    tle0 = serializers.SerializerMethodField()
    tle1 = serializers.SerializerMethodField()
    tle2 = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'ground_station', 'tle0', 'tle1', 'tle2',
                  'frequency')

    def get_frequency(self, obj):
        return obj.observation.transponder.downlink_low

    def get_tle0(self, obj):
        return obj.observation.satellite.tle0

    def get_tle1(self, obj):
        return obj.observation.satellite.tle1

    def get_tle2(self, obj):
        return obj.observation.satellite.tle2
