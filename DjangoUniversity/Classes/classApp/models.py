from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.DecimalField(default=0, max_digits=10000)
    instructorName = models.CharField(max_length=50,default="",null=False)
    duration = models.FloatField()