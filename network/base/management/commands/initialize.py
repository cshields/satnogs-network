from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Create initial fixtures'

    def handle(self, *args, **options):
        # Migrate
        call_command('migrate')

        #  Initial data
        call_command('loaddata', 'antennas')
        call_command('fetch_data')

        # Create random fixtures for remaining models
        from network.base.tests import ObservationFactory, StationFactory
        from network.base.models import Antenna
        ObservationFactory.create_batch(20)
        StationFactory.create_batch(10,
                                    antennas=(Antenna.objects.all().values_list('id', flat=True)))

        # Update TLEs
        call_command('update_all_tle')

        # Create superuser
        call_command('createsuperuser')
