from django.utils.timezone import now

from rest_framework import viewsets, mixins

from network.api.perms import StationOwnerCanViewPermission, StationOwnerCanEditPermission
from network.api import serializers, filters
from network.base.models import (Antenna, Data, Observation, Satellite,
                                 Station, Transponder)


class AntennaView(viewsets.ReadOnlyModelViewSet):
    queryset = Antenna.objects.all()
    serializer_class = serializers.AntennaSerializer


class StationView(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = serializers.StationSerializer


class SatelliteView(viewsets.ReadOnlyModelViewSet):
    queryset = Satellite.objects.all()
    serializer_class = serializers.SatelliteSerializer


class TransponderView(viewsets.ReadOnlyModelViewSet):
    queryset = Transponder.objects.all()
    serializer_class = serializers.TransponderSerializer


class ObservationView(viewsets.ReadOnlyModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = serializers.ObservationSerializer


class DataView(viewsets.ModelViewSet, mixins.UpdateModelMixin):
    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer
    permission_classes = [
        StationOwnerCanEditPermission
    ]


class JobView(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.filter(payload='')
    serializer_class = serializers.JobSerializer
    filter_class = filters.DataViewFilter
    filter_fields = ('ground_station')
    permission_classes = [
        StationOwnerCanViewPermission
    ]

    def get_queryset(self):
        return self.queryset.filter(start__gte=now())
