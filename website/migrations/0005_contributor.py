# Generated by Django 3.0.6 on 2020-05-24 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_auto_20200524_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.TextField(verbose_name='Contribution')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to=website.models.Contributor.get_photo_upload_path, verbose_name='Photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
            },
        ),
    ]
