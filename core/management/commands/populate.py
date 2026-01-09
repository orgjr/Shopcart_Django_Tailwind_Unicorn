from django.core.management.base import BaseCommand
from core.models import Product


class Command(BaseCommand):
    help = "Load product data to the database"

    def handle(self, *args, **kwargs):
        Product.objects.get_or_create(name="Figo", price=18.50)

        Product.objects.get_or_create(name="Lazanha", price=8.50)

        Product.objects.get_or_create(name="TV", price=1880.49)

        Product.objects.get_or_create(name="Air Frier", price=455.69)

        Product.objects.get_or_create(name="Algodão", price=3.50)

        Product.objects.get_or_create(name="Óleo de soja", price=8.19)
