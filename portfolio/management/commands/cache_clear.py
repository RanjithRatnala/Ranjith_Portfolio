from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings

class Command(BaseCommand):
    help = 'Clear all cache in production'

    def handle(self, *args, **options):
        try:
            # Clear all cache
            cache.clear()
            self.stdout.write(
                self.style.SUCCESS('Cache cleared successfully')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to clear cache: {e}')
            ) 