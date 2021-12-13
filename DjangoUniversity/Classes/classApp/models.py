from django.db import models


class djangoClasses(models.Model):              #creating a class
    title = models.CharField(max_length=50)     #giving attributes, different fields
    courseNumber = models.DecimalField(default=0, max_digits=10000, decimal_places=0)
    instructorName = models.CharField(max_length=50,default="", null=False)
    duration = models.FloatField(max_length=50, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.title #returns name of title to the admin page to display



