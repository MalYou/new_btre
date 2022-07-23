# Generated by Django 4.0.6 on 2022-07-23 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.state')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('name', models.CharField(max_length=201, primary_key=True, serialize=False)),
                ('zipcode', models.CharField(max_length=30, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
                ('country', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.country')),
                ('state', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.state')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
