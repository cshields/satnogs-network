from rest_framework import serializers

from network.base.models import Data, Station


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'observation', 'ground_station', 'payload', 'payload_demode')
        read_only_fields = ['id', 'start', 'end', 'observation', 'ground_station']


class JobSerializer(serializers.ModelSerializer):
    frequency = serializers.SerializerMethodField()
    tle0 = serializers.SerializerMethodField()
    tle1 = serializers.SerializerMethodField()
    tle2 = serializers.SerializerMethodField()
    mode = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'ground_station', 'tle0', 'tle1', 'tle2',
                  'frequency', 'mode')

    def get_frequency(self, obj):
        return obj.observation.transmitter.downlink_low

    def get_tle0(self, obj):
        return obj.observation.tle.tle0

    def get_tle1(self, obj):
        return obj.observation.tle.tle1

    def get_tle2(self, obj):
        return obj.observation.tle.tle2

    def get_mode(self, obj):
        try:
            return obj.observation.transmitter.mode.name
        except:
            return ''


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('uuid', 'name', 'alt', 'lat', 'lng', 'rig',
                  'active', 'antenna', 'id', 'apikey')

    apikey = serializers.CharField(read_only=True)
