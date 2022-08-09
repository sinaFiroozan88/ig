# Generated by Django 3.2.3 on 2021-06-30 13:00

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
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['food'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='تاریخ')),
                ('time', models.DateField(verbose_name='روز')),
                ('rice', models.IntegerField(blank=True, null=True, verbose_name='برنج')),
                ('beef', models.IntegerField(blank=True, null=True, verbose_name='گوشت گوساله')),
                ('lamb', models.IntegerField(blank=True, null=True, verbose_name='گوشت گوسفند')),
                ('chicken_leg', models.IntegerField(blank=True, null=True, verbose_name='ران مرغ')),
                ('chicken_breast', models.IntegerField(blank=True, null=True, verbose_name='سینه مرغ')),
                ('fish', models.IntegerField(blank=True, null=True, verbose_name='ماهی')),
                ('solid_oil', models.IntegerField(blank=True, null=True, verbose_name='روغن جامد')),
                ('liquid_oil', models.IntegerField(blank=True, null=True, verbose_name='روغن مایع')),
                ('beef_shank', models.IntegerField(blank=True, null=True, verbose_name='قلم گوساله')),
                ('olive_oil', models.IntegerField(blank=True, null=True, verbose_name='روغن زیتون')),
                ('macaroni', models.IntegerField(blank=True, null=True, verbose_name='ماکارونی')),
                ('reshte_poloie', models.IntegerField(blank=True, null=True, verbose_name='رشته پلویی')),
                ('rob_anar', models.IntegerField(blank=True, null=True, verbose_name='رب انار')),
                ('egg', models.IntegerField(blank=True, null=True, verbose_name='تخم مرغ')),
                ('animal_oil', models.IntegerField(blank=True, null=True, verbose_name='روغن حیوانی')),
                ('butter_1', models.IntegerField(blank=True, null=True, verbose_name='کره')),
                ('lemon_juice_1', models.IntegerField(blank=True, null=True, verbose_name='آبلیمو یک نفره')),
                ('butter_bulk', models.IntegerField(blank=True, null=True, verbose_name='کره فله ای')),
                ('tomato_paste', models.IntegerField(blank=True, null=True, verbose_name='رب گوجه فرنگی')),
                ('lentil', models.IntegerField(blank=True, null=True, verbose_name='عدس')),
                ('raisin', models.IntegerField(blank=True, null=True, verbose_name='کشمش')),
                ('walnut', models.IntegerField(blank=True, null=True, verbose_name='گردو')),
                ('split_peas', models.IntegerField(blank=True, null=True, verbose_name='لپه')),
                ('red_beans', models.IntegerField(blank=True, null=True, verbose_name='لوبیا قرمز')),
                ('tomato', models.IntegerField(blank=True, null=True, verbose_name='گوجه فرنگی')),
                ('onion', models.IntegerField(blank=True, null=True, verbose_name='پیاز')),
                ('potato', models.IntegerField(blank=True, null=True, verbose_name='سیب زمینی')),
                ('broad_bean', models.IntegerField(blank=True, null=True, verbose_name='باقالی')),
                ('celery', models.IntegerField(blank=True, null=True, verbose_name='کرفس')),
                ('green_bean', models.IntegerField(blank=True, null=True, verbose_name='لوبیا سبز')),
                ('eggplant', models.IntegerField(blank=True, null=True, verbose_name='بادمجان')),
                ('amani_lemon', models.IntegerField(blank=True, null=True, verbose_name='لیمو امانی')),
                ('lemon', models.IntegerField(blank=True, null=True, verbose_name='لیمو')),
                ('sabzi_kuku', models.IntegerField(blank=True, null=True, verbose_name='سبزی کوکو')),
                ('sabzi_qorme', models.IntegerField(blank=True, null=True, verbose_name='سبزی قورمه')),
                ('sabzi_poloie', models.IntegerField(blank=True, null=True, verbose_name='سبزی پلویی')),
                ('garlic', models.IntegerField(blank=True, null=True, verbose_name='سیر')),
                ('bell_pepper', models.IntegerField(blank=True, null=True, verbose_name='فلفل دلمه')),
                ('mushroom', models.IntegerField(blank=True, null=True, verbose_name='قارچ')),
                ('peas', models.IntegerField(blank=True, null=True, verbose_name='نخود فرنگی')),
                ('coriander', models.IntegerField(blank=True, null=True, verbose_name='گشنیز')),
                ('dry_savory', models.IntegerField(blank=True, null=True, verbose_name='مرزه خشک')),
                ('dried_tarragon', models.IntegerField(blank=True, null=True, verbose_name='ترخون خشک')),
                ('spearmint', models.IntegerField(blank=True, null=True, verbose_name='نعناع')),
                ('jafari', models.IntegerField(blank=True, null=True, verbose_name='جعفری')),
                ('reyhan', models.IntegerField(blank=True, null=True, verbose_name='ریحان')),
                ('pickle', models.IntegerField(blank=True, null=True, verbose_name='خیارشور')),
                ('carrot', models.IntegerField(blank=True, null=True, verbose_name='هویج')),
                ('shevid', models.IntegerField(blank=True, null=True, verbose_name='شوید')),
                ('saffron', models.IntegerField(blank=True, null=True, verbose_name='زعفران')),
                ('verjuice', models.IntegerField(blank=True, null=True, verbose_name='آبغوره')),
                ('lemon_juice', models.IntegerField(blank=True, null=True, verbose_name='آبلیمو')),
                ('white_vinegar', models.IntegerField(blank=True, null=True, verbose_name='سرکه سقید')),
                ('white_flour', models.IntegerField(blank=True, null=True, verbose_name='آرد سفید')),
                ('toasted_flour', models.IntegerField(blank=True, null=True, verbose_name='آرد سوخاری')),
                ('toasted_powder', models.IntegerField(blank=True, null=True, verbose_name='پودر سوخاری')),
                ('rice_flour', models.IntegerField(blank=True, null=True, verbose_name='آرد برنج')),
                ('chickpea_flour', models.IntegerField(blank=True, null=True, verbose_name='آرد نخود')),
                ('sugar', models.IntegerField(blank=True, null=True, verbose_name='شکر')),
                ('yogurt', models.IntegerField(blank=True, null=True, verbose_name='ماست')),
                ('sumac', models.IntegerField(blank=True, null=True, verbose_name='سماق')),
                ('starch', models.IntegerField(blank=True, null=True, verbose_name='نشاسته')),
                ('vinegar', models.IntegerField(blank=True, null=True, verbose_name='سرکه')),
                ('mustard', models.IntegerField(blank=True, null=True, verbose_name='سس خردل')),
                ('sauce', models.IntegerField(blank=True, null=True, verbose_name='سس')),
                ('rosewater', models.IntegerField(blank=True, null=True, verbose_name='گلاب')),
                ('barberry', models.IntegerField(blank=True, null=True, verbose_name='زرشک')),
                ('rock_salt', models.IntegerField(blank=True, null=True, verbose_name='سنگ نمک')),
                ('pepper', models.IntegerField(blank=True, null=True, verbose_name='فلفل')),
                ('milk', models.IntegerField(blank=True, null=True, verbose_name='شیر')),
                ('salt', models.IntegerField(blank=True, null=True, verbose_name='نمک')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'ordering': ['food'],
            },
        ),
        migrations.CreateModel(
            name='DailyMeal',
            fields=[
                ('ingredient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='canteen.ingredient')),
                ('quantity', models.IntegerField(verbose_name='تعداد غذا')),
            ],
            options={
                'ordering': ['food'],
            },
            bases=('canteen.ingredient',),
        ),
    ]
