# Generated by Django 4.0.6 on 2022-09-12 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qc_retest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qc_retest_model',
            old_name='Retained_on_200',
            new_name='retained_on_200',
        ),
        migrations.RenameField(
            model_name='qc_retest_model',
            old_name='Retained_on_500',
            new_name='retained_on_500',
        ),
        migrations.RenameField(
            model_name='qc_retest_model',
            old_name='Retained_on_63',
            new_name='retained_on_63',
        ),
    ]
