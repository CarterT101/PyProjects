from django.db import models
import datetime


TYPE_CHOICES = {
    ('deposit', 'deposit'),
    ('withdrawal', 'withdrawal'),
}

TYPE_CHOICES2 = {
    ('checkings', 'checkings'),
    ('savings', 'savings'),
}


class Account(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    balance = models.DecimalField(default=0.00, max_digits=1000000, decimal_places=2)
    transaction_date = models.DateField(default=datetime.date.today)
    transaction_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount = models.DecimalField(default=0.00, max_digits=100000, decimal_places=2)
    description = models.TextField(max_length=300, default="", blank=True)
    account = models.CharField(max_length=50, choices=TYPE_CHOICES2)

    objects = models.Manager()

    def __str__(self):
        return self.name


