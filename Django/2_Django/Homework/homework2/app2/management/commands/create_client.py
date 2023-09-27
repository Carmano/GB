from django.core.management.base import BaseCommand
from app2.models import Client


class Command(BaseCommand):
    help = 'Print "hello world" to output.'

    def handle(self, *args, **kwargs):
        client = Client(name='Tooli', email='toliy@mail.ru', number='89999001111', address='Коетова 4')
        client.save()

