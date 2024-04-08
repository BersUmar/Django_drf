from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        permissions = [30, 32, 34, 36]
        group_moder = Group.objects.create(name='moderators')
        group_moder.permissions.add(*permissions)