# Generated by Django 4.0.6 on 2022-08-05 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='realtor',
        ),
    ]
