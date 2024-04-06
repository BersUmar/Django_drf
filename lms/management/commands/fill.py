from django.core.management import BaseCommand
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {
                "user": User.objects.get(1),
                "paid_lesson": 1,
                "payment_amount": 20.00,
                "payment_method": "PayPal"
            },
            {
                "user": User.objects.get(1),
                "paid_course": 1,
                "payment_amount": 150.00,
                "payment_method": "Bank Transfer"
            },
            {
                "user": User.objects.get(1),
                "paid_course": 1,
                "payment_amount": 120.00,
                "payment_method": "Debit Card"
            },
            {
                "user": User.objects.get(1),
                "paid_course": 1,
                "payment_amount": 75.00,
                "payment_method": "PayPal"
            },
            {
                "user": User.objects.get(1),
                "paid_course_id": 1,
                "payment_amount": 50.00,
                "payment_method": "Credit Card"
            }

        ]

        payments_for_create = []
        for payment in payments_list:
            payments_for_create.append(
                Payments(**payment)
            )

        Payments.objects.bulk_create(payments_for_create)
