# Generated by Django 2.1.7 on 2019-04-01 19:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='url',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')]),
        ),
    ]