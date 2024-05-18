from django.core.management.base import BaseCommand
from authapp.models import StreamUser
from authapp.models import StreamUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = StreamUser.objects.all()
        for user in users:
            users_profile = StreamUserProfile.objects.create(user=user)
            users_profile.save()
