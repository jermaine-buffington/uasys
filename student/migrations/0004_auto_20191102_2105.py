# Generated by Django 2.0.7 on 2019-11-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191102_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.TextField(null=True),
        ),
    ]
