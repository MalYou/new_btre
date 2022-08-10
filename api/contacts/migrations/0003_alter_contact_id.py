# Generated by Django 4.0.6 on 2022-08-06 21:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contact_realtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]