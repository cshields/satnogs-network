from django.contrib import admin

from network.base.models import (Antenna, Satellite, Station, Transponder,
                                 Observation, Data)


class AntennaAdmin(admin.ModelAdmin):
    list_display = ('antenna_type', 'frequency', 'band')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'lng', 'lat')


class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'norad_cat_id')


class TransponderAdmin(admin.ModelAdmin):
    list_display = ('satellite', 'description', 'uplink_low',
                    'uplink_high', 'downlink_low', 'downlink_high')


class ObservasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'satellite', 'transponder', 'start', 'end')


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'observation', 'ground_station')

admin.site.register(Antenna, AntennaAdmin)
admin.site.register(Satellite, SatelliteAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Transponder, TransponderAdmin)
admin.site.register(Observation, ObservasionAdmin)
admin.site.register(Data, DataAdmin)
