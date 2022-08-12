from django.db import models


class product_report(models.Model):
    # crasher operation
    Machinery = models.DurationField()
    Crasher_Elec_Consumption = models.IntegerField()
    No_Needed = models.DurationField()
    Electrical_Fault = models.DurationField()
    Mechanical_Fault = models.DurationField()
    Operator_Fault = models.DurationField()
    Total_Fault = models.IntegerField(editable=False)
    # Raw Material Consumption
    Kenaf_Rawmat_Consumption = models.IntegerField(max_length=4)
    Kenaf_Stucco_Prod_1 = models.IntegerField(max_length=4)
    Kenaf_Stucco_Prod_2 = models.IntegerField(max_length=4)
    Ordinary_RawMat_Consumption_1 = models.IntegerField(max_length=4)
    Ordinary_RawMat_Consumption_2 = models.IntegerField(max_length=4)
    Ordinary_Stucco_Prod_1 = models.IntegerField(max_length=4)
    Ordinary_Stucco_Prod_2 = models.IntegerField(max_length=4)
    Block_RawMat_Consumption_1 = models.IntegerField(max_length=4)
    Block_RawMat_Consumption_2 = models.IntegerField(max_length=4)
    Nealit_RawMat_Consumption = models.IntegerField(max_length=4)
    Nealit_Sugar_Consumption = models.IntegerField(max_length=4)
    Nealit_Prod = models.IntegerField(max_length=4)
    Total_Consumption = models.IntegerField(editable=False)
    Total_Prod = models.IntegerField(editable=False)
    # stoppage causes
    No_Needed_1 = models.DurationField()
    No_Needed_2 = models.DurationField()
    No_Needed_Nealit = models.DurationField()
    Electrical_Stoppage_1 = models.DurationField()
    Electrical_Stoppage_2 = models.DurationField()
    Electrical_Stoppage_Nealit = models.DurationField()
    Mechanical_Stoppage_1 = models.DurationField()
    Mechanical_Stoppage_2 = models.DurationField()
    Mechanical_Stoppage_Nealit = models.DurationField()
    Blackout_Stoppage_1 = models.DurationField()
    Blackout_Stoppage_2 = models.DurationField()
    Blackout_Stoppage_Nealit = models.DurationField()
    Gas_Cutout_Stoppage_1 = models.DurationField()
    Gas_Cutout_Stoppage_2 = models.DurationField()
    Gas_Cutout_Stoppage_Nealit = models.DurationField()
    Gasoil_Cutout_Stoppage_1 = models.DurationField()
    Gasoil_Cutout_Stoppage_2 = models.DurationField()
    Gasoil_Cutout_Stoppage_Nealit = models.DurationField()
    Initial_Start_Stoppage_1 = models.DurationField()
    Initial_Start_Stoppage_2 = models.DurationField()
    Initial_Start_Stoppage_Nealit = models.DurationField()
    End_production_Stoppage_1 = models.DurationField()
    End_production_Stoppage_2 = models.DurationField()
    End_production_Stoppage_Nealit = models.DurationField()
    Operator_Base_Stoppage_1 = models.DurationField()
    Operator_Base_Stoppage_2 = models.DurationField()
    Operator_Base_Stoppage_Nealit = models.DurationField()
    Total_Stoppage_1 = models.DurationField()
    Total_Stoppage_2 = models.DurationField()
    Total_Stoppage_Nealit = models.DurationField()
    # silo inventories
    Silo_1_Inventory = models.IntegerField(max_length=4)
    Silo_2_Inventory = models.IntegerField(max_length=4)
    Block_Silo_N_Inventory = models.IntegerField(max_length=4)
    Block_Silo_S_Inventory = models.IntegerField(max_length=4)
    Silo_800_Inventory = models.IntegerField(max_length=4)
    # energy consumption
    Gas_Consumption_AM_1 = models.IntegerField(max_length=4)
    Gas_Consumption_PM_1 = models.IntegerField(max_length=4)
    Gas_Consumption_AM_2 = models.IntegerField(max_length=4)
    Gas_Consumption_PM_2 = models.IntegerField(max_length=4)
    Gasoil_Consumption_AM_1 = models.IntegerField(max_length=4)
    Gasoil_Consumption_PM_1 = models.IntegerField(max_length=4)
    Gasoil_Consumption_AM_2 = models.IntegerField(max_length=4)
    Gasoil_Consumption_PM_2 = models.IntegerField(max_length=4)
    Gas_Temperature_1 = models.IntegerField(max_length=4)
    Gas_Temperature_2 = models.IntegerField(max_length=4)
    Gas_Presure_1 = models.IntegerField(max_length=4)
    Gas_Presure_2 = models.IntegerField(max_length=4)
