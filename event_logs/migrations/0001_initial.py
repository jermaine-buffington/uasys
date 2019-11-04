# Generated by Django 2.0.7 on 2019-10-27 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Logs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_date', models.DateField()),
                ('title', models.TextField()),
                ('location', models.TextField()),
                ('host', models.TextField()),
                ('_start', models.CharField(max_length=8)),
                ('_end', models.CharField(max_length=8)),
            ],
        ),
    ]
