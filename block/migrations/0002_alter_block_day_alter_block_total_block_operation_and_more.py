# Generated by Django 4.0.6 on 2022-08-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یکشنبه', 'یکشنبه'), ('دوشنبه', 'دوشنبه'), ('سه شنبه', 'سه شنبه'), ('چهارشنبه', 'چهارشنبه'), ('پنجشنبه', 'پنجشنبه'), ('جمعه', 'جمعه')], max_length=8, verbose_name='روز'),
        ),
        migrations.AlterField(
            model_name='block',
            name='total_block_operation',
            field=models.IntegerField(blank=True, null=True, verbose_name='جمع کل'),
        ),
        migrations.AlterField(
            model_name='block',
            name='total_block_packing',
            field=models.IntegerField(blank=True, null=True, verbose_name='جمع کل'),
        ),
        migrations.AlterField(
            model_name='block',
            name='total_block_prod',
            field=models.IntegerField(blank=True, null=True, verbose_name='جمع کل'),
        ),
        migrations.AlterField(
            model_name='block',
            name='total_block_waste',
            field=models.IntegerField(blank=True, null=True, verbose_name='جمع کل'),
        ),
    ]
