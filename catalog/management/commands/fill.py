from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'c_name': 'продукты', 'c_description': 'описание продукты'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

            Category.objects.all().delete()
            Category.objects.bulk_create(category_for_create)
