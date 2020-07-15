from django.core.management import BaseCommand
from account.models import SavingAccount, CheckingAccount
from customer.models import Customer
from branch.models import Branch, Staff
from djmoney.money import Money
import faker
import random


class Command(BaseCommand):
    help = 'populate database with random accounts. please first insert customers, branches and staff'

    def handle(self, *args, **options):
        fake = faker.Faker(['zh_CN'])

        staff_count = Staff.objects.count()

        for customer in Customer.objects.all():
            for branch in Branch.objects.all():
                SavingAccount.objects.create(
                    balance=Money(amount=random.uniform(1000, 1000000), currency='CNY'),
                    date_opened=fake.date_between(start_date='-10y', end_date='today'),
                    branch=branch,
                    customer=customer,
                    manager=Staff.objects.all()[random.randint(0, staff_count - 1)],
                    interest_rate=random.uniform(0, 0.1)
                )

                CheckingAccount.objects.create(
                    balance=Money(amount=random.uniform(1000, 1000000), currency='CNY'),
                    date_opened=fake.date_between(start_date='-10y', end_date='today'),
                    branch=branch,
                    customer=customer,
                    manager=Staff.objects.all()[random.randint(0, staff_count - 1)],
                    overdraft=Money(amount=random.uniform(1000, 1000000), currency='CNY'),
                )
