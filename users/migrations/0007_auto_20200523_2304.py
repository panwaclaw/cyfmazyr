# Generated by Django 3.0.6 on 2020-05-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200523_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_year',
            field=models.PositiveIntegerField(verbose_name='Admission Year'),
        ),
    ]
