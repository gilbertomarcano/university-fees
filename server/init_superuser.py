from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='admin@admin.com').exists():
            User.objects.create_superuser(
                username='admin@admin.com',
                password='admin',
                email='admin@admin.com',
            )