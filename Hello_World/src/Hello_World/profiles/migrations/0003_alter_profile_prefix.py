# Generated by Django 4.0 on 2021-12-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mr', 'Mr')], default='', max_length=10),
        ),
    ]
