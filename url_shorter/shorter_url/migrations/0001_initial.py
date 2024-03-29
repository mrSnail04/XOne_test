# Generated by Django 4.0.6 on 2022-07-11 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_long', models.URLField(max_length=2048, verbose_name='Url long')),
                ('url_short', models.URLField(max_length=256, unique=True, verbose_name='Url short')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_url', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'UrlStorage',
                'verbose_name_plural': 'Films genre',
            },
        ),
        migrations.AddConstraint(
            model_name='urlstorage',
            constraint=models.UniqueConstraint(fields=('owner', 'url_long'), name='owner_url_long'),
        ),
    ]
