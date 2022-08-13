from django import forms
from django.forms import widgets

from block.models import Block


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = (
            'day', 'date', 'block_stucco', 'water_consumption', 'gas_consumption', 'elec_consumption',
            'gasoil_consumption', 'block7_prod', 'block8_prod', 'block8mr_prod', 'total_block_prod', 'block7_packing',
            'block8_packing',
            'block8mr_packing', 'total_block_packing', 'block7_waste', 'block8_waste', 'block8mr_waste',
            'total_block_waste', 'block7_operation', 'block8_operation', 'dryer_operation', 'total_block_operation',
            'block7_packing_inventory', 'block7_dryer_inventory', 'block7_rack_inventory', 'block8_packing_inventory',
            'block8_dryer_inventory', 'block8_rack_inventory', 'block8mr_packing_inventory', 'block8mr_dryer_inventory',
            'block8mr_rack_inventory', 'block7_rawmat_stoppage', 'block7_operator_stoppage',
            'block7_mechanical_stoppage',
            'block7_electrical_stoppage', 'block7_noNeeded_stoppage', 'block7_rackFull_stoppage',
            'block7_gasoil_stoppage', 'block7_gas_stoppage', 'block7_elec_stoppage', 'block7_total_stoppage',
            'block8_rawmat_stoppage',
            'block8_operator_stoppage', 'block8_mechanical_stoppage', 'block8_electrical_stoppage',
            'block8_noNeeded_stoppage', 'block8_rackFull_stoppage', 'block8_gasoil_stoppage',
            'block8_gas_stoppage', 'block8_elec_stoppage', 'block8_total_stoppage', 'dryer_rawmat_stoppage',
            'dryer_operator_stoppage', 'dryer_mechanical_stoppage', 'dryer_electrical_stoppage',
            'dryer_noNeeded_stoppage', 'dryer_rackFull_stoppage', 'dryer_gasoil_stoppage',
            'dryer_gas_stoppage', 'dryer_elec_stoppage', 'dryer_total_stoppage','betogips_inventory', 'betogips_wased')
        widget = {
            'day': widgets.Select(),
            'date': widgets.DateInput(),
            'block_stucco': widgets.NumberInput(),
            'water_consumption': widgets.NumberInput(),
            'gas_consumption': widgets.NumberInput(),
            'elec_consumption': widgets.NumberInput(),
            'gasoil_consumption': widgets.NumberInput(),
            'block7_prod': widgets.NumberInput(),
            'block8_prod': widgets.NumberInput(),
            'block8mr_prod': widgets.NumberInput(),
            'total_block_prod': widgets.NumberInput(),
            'block7_packing': widgets.NumberInput(),
            'block8_packing': widgets.NumberInput(),
            'block8mr_packing': widgets.NumberInput(),
            'total_block_packing': widgets.NumberInput(),
            'block7_waste': widgets.NumberInput(),
            'block8_waste': widgets.NumberInput(),
            'block8mr_waste': widgets.NumberInput(),
            'total_block_waste': widgets.NumberInput(),
            'block7_operation': widgets.NumberInput(),
            'block8_operation': widgets.NumberInput(),
            'dryer_operation': widgets.NumberInput(),
            'total_block_operation': widgets.NumberInput(),
            'block7_packing_inventory': widgets.NumberInput(),
            'block7_dryer_inventory': widgets.NumberInput(),
            'block7_rack_inventory': widgets.NumberInput(),
            'block8_packing_inventory': widgets.NumberInput(),
            'block8_dryer_inventory': widgets.NumberInput(),
            'block8_rack_inventory': widgets.NumberInput(),
            'block8mr_packing_inventory': widgets.NumberInput(),
            'block8mr_dryer_inventory': widgets.NumberInput(),
            'block8mr_rack_inventory': widgets.NumberInput(),
            'block7_rawmat_stoppage': widgets.NumberInput(),
            'block7_operator_stoppage': widgets.NumberInput(),
            'block7_mechanical_stoppage': widgets.NumberInput(),
            'block7_electrical_stoppage': widgets.NumberInput(),
            'block7_noNeeded_stoppage': widgets.NumberInput(),
            'block7_rackFull_stoppage': widgets.NumberInput(),
            'block7_gasoil_stoppage': widgets.NumberInput(),
            'block7_gas_stoppage': widgets.NumberInput(),
            'block7_elec_stoppage': widgets.NumberInput(),
            'block7_total_stoppage': widgets.NumberInput(),
            'block8_rawmat_stoppage': widgets.NumberInput(),
            'block8_operator_stoppage': widgets.NumberInput(),
            'block8_mechanical_stoppage': widgets.NumberInput(),
            'block8_electrical_stoppage': widgets.NumberInput(),
            'block8_noNeeded_stoppage': widgets.NumberInput(),
            'block8_rackFull_stoppage': widgets.NumberInput(),
            'block8_gasoil_stoppage': widgets.NumberInput(),
            'block8_gas_stoppage': widgets.NumberInput(),
            'block8_elec_stoppage': widgets.NumberInput(),
            'block8_total_stoppage': widgets.NumberInput(),
            'dryer_rawmat_stoppage': widgets.NumberInput(),
            'dryer_operator_stoppage': widgets.NumberInput(),
            'dryer_mechanical_stoppage': widgets.NumberInput(),
            'dryer_electrical_stoppage': widgets.NumberInput(),
            'dryer_noNeeded_stoppage': widgets.NumberInput(),
            'dryer_rackFull_stoppage': widgets.NumberInput(),
            'dryer_gasoil_stoppage': widgets.NumberInput(),
            'dryer_gas_stoppage': widgets.NumberInput(),
            'dryer_elec_stoppage': widgets.NumberInput(),
            'dryer_total_stoppage': widgets.NumberInput(),
            'betogips_inventory': widgets.NumberInput(),
            'betogips_wased': widgets.NumberInput()
        }
