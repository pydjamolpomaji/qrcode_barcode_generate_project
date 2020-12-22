from django import forms
from .models import QR_Code_Model


class qrcode_form(forms.ModelForm):
    class Meta:
        model = QR_Code_Model
        fields = ('name',)
