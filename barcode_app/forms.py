from django import forms
from .models import Barcode_Model


class BarcodeModelForm(forms.ModelForm):
    class Meta:
        model = Barcode_Model
        fields = ['name', 'country_id', 'manufacturer_id', 'number_id']
