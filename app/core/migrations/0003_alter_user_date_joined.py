# Generated by Django 3.2.20 on 2023-07-16 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
