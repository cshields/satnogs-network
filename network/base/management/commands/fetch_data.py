import json
import urllib2

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from network.base.models import Satellite, Transponder


class Command(BaseCommand):
    help = 'Provide DB API endpoint'

    def handle(self, *args, **options):
        apiurl = settings.DB_API_ENDPOINT
        satellites_url = "{0}satellites".format(apiurl)
        transponders_url = "{0}transponders".format(apiurl)
        self.stdout.write(satellites_url)
        try:
            satellites = urllib2.urlopen(satellites_url).read()
            transponders = urllib2.urlopen(transponders_url).read()
        except:
            raise CommandError('API is unreachable')

        for satellite in json.loads(satellites):
            norad_cat_id = satellite['norad_cat_id']
            name = satellite['name']
            try:
                sat = Satellite.objects.get(norad_cat_id=norad_cat_id)
                self.stdout.write('Satellite {0} already exists'.format(norad_cat_id))
            except:
                sat = Satellite(norad_cat_id=norad_cat_id, name=name)
                sat.save()
                self.stdout.write('Satellite {0} added'.format(norad_cat_id))

        for transponder in json.loads(transponders):
            norad_cat_id = transponder['norad_cat_id']
            uuid = transponder['uuid']

            try:
                sat = Satellite.objects.get(norad_cat_id=norad_cat_id)
            except:
                self.stdout.write('Satellite {0} not present'.format(norad_cat_id))
            transponder.pop('norad_cat_id')
            try:
                existing_transponder = Transponder.objects.get(uuid=uuid)
                existing_transponder.__dict__.update(transponder)
                existing_transponder.satellite = sat
                self.stdout.write('Transponder {0} updated'.format(uuid))
            except Transponder.DoesNotExist:
                new_transponder = Transponder.objects.create(**transponder)
                new_transponder.satellite = sat
                new_transponder.save()
                self.stdout.write('Transponder {0} created'.format(uuid))
