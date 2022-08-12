from django.db import models


class Block(models.Model):
    days = (
            (0, 'شنبه'),
            (1, 'یکشنبه'),
            (2, 'دوشنبه'),
            (3, 'سه شنبه'),
            (4, 'چهارشنبه'),
            (5, 'پنجشنبه'),
            (6, 'جمعه')
            )
    day = models.CharField(verbose_name='روز', max_length=8, choices=days)
    date = models.DateField(verbose_name='تاریخ',)
    # consumption
    block_stucco = models.IntegerField(verbose_name='مصرف گچ (تن)')
    water_consumption = models.IntegerField(verbose_name='مصرف آب (لیتر)')
    gas_consumption = models.IntegerField(verbose_name='مصرف گاز (متر مکعب)')
    elec_consumption = models.IntegerField(verbose_name='مصرف برق (کیلو وات)')
    gasoil_consumption = models.IntegerField(verbose_name='مصرف گازوئیل (لیتر)')
    # production
    block7_prod = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_prod = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_prod = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_prod = models.IntegerField(verbose_name='جمع کل')
    # packing
    block7_packing = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_packing = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_packing = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_packing = models.IntegerField(verbose_name='جمع کل')
    # packing waste
    block7_waste = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_waste = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_waste = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_waste = models.IntegerField(verbose_name='جمع کل')
    # block machinery
    block7_operation = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_operation = models.IntegerField(verbose_name='بلوک 8 سانت')
    dryer_operation = models.IntegerField(verbose_name='خشک کن')
    total_block_operation = models.IntegerField(verbose_name='جمع کل')
    # block inventory
    block7_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 7')
    block7_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 7")
    block7_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 7")

    block8_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 8')
    block8_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 8")
    block8_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 8")

    block8mr_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 8 عایق')
    block8mr_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 8 عایق")
    block8mr_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 8 عایق")
    # block stoppage
    block7_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    block7_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    block7_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    block7_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    block7_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    block7_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    block7_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    block7_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    block7_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    block7_gas_stoppage = models.IntegerField(verbose_name='گاز')
    block7_elec_stoppage = models.IntegerField(verbose_name='برق')
    block7_total_stoppage = models.IntegerField(verbose_name='جمع توقفات')

    block8_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    block8_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    block8_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    block8_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    block8_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    block8_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    block8_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    block8_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    block8_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    block8_gas_stoppage = models.IntegerField(verbose_name='گاز')
    block8_elec_stoppage = models.IntegerField(verbose_name='برق')
    block8_total_stoppage = models.IntegerField(verbose_name='جمع توقفات')

    dryer_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    dryer_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    dryer_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    dryer_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    dryer_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    dryer_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    dryer_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    dryer_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    dryer_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    dryer_gas_stoppage = models.IntegerField(verbose_name='گاز')
    dryer_elec_stoppage = models.IntegerField(verbose_name='برق')
    dryer_total_stoppage = models.IntegerField(verbose_name='جمع توقفات')
