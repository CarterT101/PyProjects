from django.db import models


TYPE_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
}


class Profile(models.Model):
    prefix = models.CharField(max_length=10, default="", choices=TYPE_CHOICES)
    first_name = models.CharField(max_length=60, default="", null=False)
    last_name = models.CharField(max_length=60, default="", null=False)
    email = models.CharField(max_length=60, default="", null=False)
    username = models.CharField(max_length=60, default="", null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name
