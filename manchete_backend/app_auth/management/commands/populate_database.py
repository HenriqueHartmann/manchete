from django.core.management import BaseCommand
from .create_groups import create_groups


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_groups()
