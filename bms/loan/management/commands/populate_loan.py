from django.core.management import BaseCommand
from customer.models import Customer
from branch.models import Branch, Staff
from djmoney.money import Money
from loan.models import Loan, LoanPayment
import faker
import random


class Command(BaseCommand):
    help = 'populate database with random loan & loan payments'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, nargs=1)

    def handle(self, *args, **options):
        fake = faker.Faker(['zh_CN'])

        for _ in range(0, options['n'][0]):
            customer_count = random.randint(1, 10)
            customers = Customer.objects.order_by('?')[:customer_count]
            loan = Loan.objects.create(
                amount=Money(amount=random.uniform(1000, 1000000), currency='CNY'),
                branch=Branch.objects.order_by('?')[0],
            )
            loan.customers.set(customers)
            loan.save()

        for loan in Loan.objects.all():
            dest_state = random.choice(['full', 'half', 'empty'])

            if dest_state == 'empty':
                continue

            payment_count = random.randint(1, 10)
            for _ in range(0, payment_count - 1):
                amount = random.uniform(0, loan.remained / 2)
                LoanPayment.objects.create(
                    amount=amount,
                    loan=loan,
                    date=fake.date_between('-10y', 'today'),
                )

            if dest_state == 'full':
                LoanPayment.objects.create(
                    amount=loan.remained,
                    loan=loan,
                    date=fake.date_between('-10y', 'today'),
                )
            else:
                amount = random.uniform(0, loan.remained / 2)
                LoanPayment.objects.create(
                    amount=amount,
                    loan=loan,
                    date=fake.date_between('-10y', 'today'),
                )
