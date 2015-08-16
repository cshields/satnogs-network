from django.contrib import admin

from network.base.models import (Antenna, Satellite, Station, Transmitter,
                                 Observation, Data)


class AntennaAdmin(admin.ModelAdmin):
    list_filter = ('band', 'antenna_type')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'lng', 'lat', 'qthlocator',
                    'created_date', 'active', 'state')
    list_filter = ('active', 'created')

    def created_date(self, obj):
        return obj.created.strftime('%d.%m.%Y, %H:%M')


class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'norad_cat_id', 'updated_date')

    def updated_date(self, obj):
        return obj.updated.strftime('%d.%m.%Y, %H:%M')


class TransmitterAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'description', 'satellite', 'uplink_low',
                    'uplink_high', 'downlink_low', 'downlink_high')
    search_fields = ('satellite', 'uuid')
    list_filter = ('mode', 'invert', 'uuid')


class ObservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'satellite', 'transmitter', 'start_date', 'end_date')
    list_filter = ('start', 'end')
    search_fields = ('satellite', 'author')

    def start_date(self, obj):
        return obj.start.strftime('%d.%m.%Y, %H:%M')

    def end_date(self, obj):
        return obj.end.strftime('%d.%m.%Y, %H:%M')


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'observation', 'ground_station')
    readonly_fields = ('observation', 'ground_station')

    def start_date(self, obj):
        return obj.start.strftime('%d.%m.%Y, %H:%M')

    def end_date(self, obj):
        return obj.end.strftime('%d.%m.%Y, %H:%M')


admin.site.register(Antenna, AntennaAdmin)
admin.site.register(Satellite, SatelliteAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Transmitter, TransmitterAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Data, DataAdmin)
