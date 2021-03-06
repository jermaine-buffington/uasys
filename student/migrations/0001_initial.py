# Generated by Django 2.0.7 on 2019-10-30 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.TextField()),
                ('first_name', models.TextField()),
                ('middle_initial', models.TextField()),
                ('last_name', models.TextField()),
                ('level', models.CharField(choices=[('FR', 'FRESHMAN'), ('SP', 'SOPHOMORE'), ('JR', 'JUNIOR'), ('SR', 'SENIOR')], max_length=2)),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('us_state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('phone', models.CharField(max_length=14)),
                ('country_code', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('ssan', models.CharField(max_length=11)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.CharField(max_length=6)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program')),
            ],
        ),
    ]
