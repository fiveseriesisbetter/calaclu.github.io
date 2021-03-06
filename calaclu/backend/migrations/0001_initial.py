# Generated by Django 3.1.3 on 2020-11-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('date', models.DateField(null=True)),
                ('time', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('host_committee', models.CharField(max_length=30)),
                ('event_page', models.URLField(blank=True)),
            ],
        ),
    ]
