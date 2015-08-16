from django.conf import settings
from django.contrib.sites.models import Site
from rest_framework import serializers

from network.base.models import Data


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
        return obj.observation.transmitter.downlink_low

    def get_tle0(self, obj):
        return obj.observation.satellite.tle0

    def get_tle1(self, obj):
        return obj.observation.satellite.tle1

    def get_tle2(self, obj):
        return obj.observation.satellite.tle2
