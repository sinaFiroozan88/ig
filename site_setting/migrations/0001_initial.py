# Generated by Django 3.2.3 on 2021-06-30 13:00

from django.db import migrations, models
import site_setting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=50, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=50, verbose_name='تلفن همراه')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('about_us', models.TextField(blank=True, null=True, verbose_name='درباره ما')),
                ('copy_right', models.CharField(blank=True, max_length=200, null=True, verbose_name='متن کپی رایت')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to=site_setting.models.upload_image_path, verbose_name='تصویر لوگو')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
            },
        ),
    ]