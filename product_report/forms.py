from django import forms
from django.forms import widgets

from product_report.models import ProductReport


class BlockForm(forms.ModelForm):
    class Meta:
        model = ProductReport
        fields = (
            'day', 'Machinery', 'Crasher_Elec_Consumption', 'No_Needed', 'Electrical_Fault', 'Mechanical_Fault',
            'Operator_Fault', 'Total_Fault',
            'Kenaf_Rawmat_Consumption', 'Kenaf_Stucco_Prod_1', 'Kenaf_Stucco_Prod_2', 'Ordinary_RawMat_Consumption_1',
            'Ordinary_RawMat_Consumption_2', 'Ordinary_Stucco_Prod_1', 'Ordinary_Stucco_Prod_2',
            'Block_RawMat_Consumption_1', 'Block_RawMat_Consumption_2', 'Nealit_RawMat_Consumption',
            'Nealit_Sugar_Consumption', 'Nealit_Prod', 'Total_Consumption', 'Total_Prod_1', 'Total_Prod_2',

            'No_Needed_1', 'No_Needed_Nealit', 'No_Needed_2', 'Electrical_Stoppage_1', 'Electrical_Stoppage_2',
            'Blackout_Stoppage_1', 'Blackout_Stoppage_2', 'Blackout_Stoppage_Nealit', 'Electrical_Stoppage_Nealit',
            'Mechanical_Stoppage_1', 'Mechanical_Stoppage_2', 'Mechanical_Stoppage_Nealit', 'Gas_Cutout_Stoppage_1',
            'Gas_Cutout_Stoppage_2', 'Gas_Cutout_Stoppage_Nealit', 'Gasoil_Cutout_Stoppage_1',
            'Gasoil_Cutout_Stoppage_2', 'Gasoil_Cutout_Stoppage_Nealit', 'Initial_Start_Stoppage_1',
            'Initial_Start_Stoppage_2', 'Initial_Start_Stoppage_Nealit',
            'End_production_Stoppage_1', 'End_production_Stoppage_2', 'End_production_Stoppage_Nealit',
            'Operator_Base_Stoppage_1', 'Operator_Base_Stoppage_2', 'Operator_Base_Stoppage_Nealit',
            'Total_Stoppage_1', 'Total_Stoppage_2', 'Total_Stoppage_Nealit',
            'Silo_1_Inventory', 'Silo_2_Inventory', 'Block_Silo_N_Inventory', 'Block_Silo_S_Inventory',
            'Silo_800_Inventory', 'Gas_Consumption_AM_1', 'Gas_Consumption_AM_2',
            'Gas_Consumption_PM_1', 'Gas_Consumption_PM_2', 'Gasoil_Consumption_AM_1', 'Gasoil_Consumption_AM_2', 'Gasoil_Consumption_PM_1',
            'Gasoil_Consumption_PM_2', 'Gas_Temperature_1', 'Gas_Temperature_2', 'Gas_Presure_1', 'Gas_Presure_2'
        )
        widget = {
            'day': widgets.Select(),
            'Machinery': widgets.DateInput(),
            'Crasher_Elec_Consumption': widgets.NumberInput(),
            'No_Needed': widgets.NumberInput(),
            'Electrical_Fault': widgets.NumberInput(),
            'Mechanical_Fault': widgets.NumberInput(),
            'Operator_Fault': widgets.NumberInput(),
            'Total_Fault': widgets.NumberInput(),
            'Kenaf_Rawmat_Consumption': widgets.NumberInput(),
            'Kenaf_Stucco_Prod_1': widgets.NumberInput(),
            'Kenaf_Stucco_Prod_2': widgets.NumberInput(),
            'Ordinary_RawMat_Consumption_1': widgets.NumberInput(),
            'Ordinary_RawMat_Consumption_2': widgets.NumberInput(),
            'Ordinary_Stucco_Prod_1': widgets.NumberInput(),
            'Ordinary_Stucco_Prod_2': widgets.NumberInput(),
            'Block_RawMat_Consumption_1': widgets.NumberInput(),
            'Block_RawMat_Consumption_2': widgets.NumberInput(),
            'Nealit_RawMat_Consumption': widgets.NumberInput(),
            'Nealit_Sugar_Consumption': widgets.NumberInput(),
            'Nealit_Prod': widgets.NumberInput(),
            'Total_Consumption': widgets.NumberInput(),
            'Total_Prod_1': widgets.NumberInput(),
            'Total_Prod_2': widgets.NumberInput(),
            'No_Needed_1': widgets.NumberInput(),
            'No_Needed_2': widgets.NumberInput(),
            'No_Needed_Nealit': widgets.NumberInput(),
            'Electrical_Stoppage_1': widgets.NumberInput(),
            'Electrical_Stoppage_2': widgets.NumberInput(),
            'Blackout_Stoppage_1': widgets.NumberInput(),
            'Blackout_Stoppage_2': widgets.NumberInput(),
            'Blackout_Stoppage_Nealit': widgets.NumberInput(),
            'Electrical_Stoppage_Nealit': widgets.NumberInput(),
            'Mechanical_Stoppage_1': widgets.NumberInput(),
            'Mechanical_Stoppage_2': widgets.NumberInput(),
            'Mechanical_Stoppage_Nealit': widgets.NumberInput(),
            'Gas_Cutout_Stoppage_1': widgets.NumberInput(),
            'Gas_Cutout_Stoppage_2': widgets.NumberInput(),
            'Gas_Cutout_Stoppage_Nealit': widgets.NumberInput(),
            'Gasoil_Cutout_Stoppage_1': widgets.NumberInput(),
            'Gasoil_Cutout_Stoppage_2': widgets.NumberInput(),
            'Gasoil_Cutout_Stoppage_Nealit': widgets.NumberInput(),
            'Initial_Start_Stoppage_1': widgets.NumberInput(),
            'Initial_Start_Stoppage_2': widgets.NumberInput(),
            'Initial_Start_Stoppage_Nealit': widgets.NumberInput(),
            'End_production_Stoppage_1': widgets.NumberInput(),
            'End_production_Stoppage_2': widgets.NumberInput(),
            'End_production_Stoppage_Nealit': widgets.NumberInput(),
            'Operator_Base_Stoppage_1': widgets.NumberInput(),
            'Operator_Base_Stoppage_2': widgets.NumberInput(),
            'Operator_Base_Stoppage_Nealit': widgets.NumberInput(),
            'Total_Stoppage_1': widgets.NumberInput(),
            'Total_Stoppage_2': widgets.NumberInput(),
            'Total_Stoppage_Nealit': widgets.NumberInput(),
            'Silo_1_Inventory': widgets.NumberInput(),
            'Silo_2_Inventory': widgets.NumberInput(),
            'Block_Silo_N_Inventory': widgets.NumberInput(),
            'Block_Silo_S_Inventory': widgets.NumberInput(),
            'Silo_800_Inventory': widgets.NumberInput(),
            'Gas_Consumption_AM_1': widgets.NumberInput(),
            'Gas_Consumption_AM_2': widgets.NumberInput(),
            'Gas_Consumption_PM_1': widgets.NumberInput(),
            'Gas_Consumption_PM_2': widgets.NumberInput(),
            'Gasoil_Consumption_AM_1': widgets.NumberInput(),
            'Gasoil_Consumption_AM_2': widgets.NumberInput(),
            'Gasoil_Consumption_PM_1': widgets.NumberInput(),
            'Gasoil_Consumption_PM_2': widgets.NumberInput(),
            'Gas_Temperature_1': widgets.NumberInput(),
            'Gas_Temperature_2': widgets.NumberInput(),
            'Gas_Presure_1': widgets.NumberInput(),
            'Gas_Presure_2': widgets.NumberInput()
        }
