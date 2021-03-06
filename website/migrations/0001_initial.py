# Generated by Django 3.0.6 on 2020-05-23 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HallOfFameMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('achievement', models.TextField(verbose_name='Achievement')),
                ('photo', models.ImageField(upload_to=website.models.HallOfFameMember.get_photo_upload_path, verbose_name='Photo')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]
