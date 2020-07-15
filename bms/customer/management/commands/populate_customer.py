from django.core.management.base import BaseCommand, CommandError
from customer.models import Customer
import faker
import random


class Command(BaseCommand):
    help = 'populate database with random customer information'

    relationships = [
        '父亲',
        '母亲',
        '朋友',
        '哥哥',
        '弟弟',
        '妹妹',
        '姐姐',
        '亲戚',
    ]

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, nargs=1)

    def handle(self, *args, **options):
        fake = faker.Faker(['zh_CN'])
        for _ in range(0, options['n'][0]):
            Customer.objects.create(
                card_id=fake.ssn(),
                name=fake.name(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                contact_name=fake.name(),
                contact_phone_number=fake.phone_number(),
                contact_email=fake.email(),
                contact_relationship=random.choice(self.relationships)
            )
