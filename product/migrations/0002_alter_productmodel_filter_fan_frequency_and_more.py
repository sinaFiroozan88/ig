# Generated by Django 4.0.6 on 2022-09-05 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='filter_fan_frequency',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(15, 'enter a number from 15 to 55'), django.core.validators.MaxValueValidator(55, 'enter a number from 15 to 55')]),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='kiln_negative_presure',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'enter a number from 0 to 0.7'), django.core.validators.MaxValueValidator(0.7, 'enter a number from 0 to 0.7')]),
        ),
    ]
