from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



class Barcode_Model(models.Model):
    name = models.CharField(max_length=200)
    barcode_name = models.ImageField(upload_to='Barcode_Images/%Y/%m/%d', blank=True)
    country_id = models.CharField(max_length=3, null=True)
    manufacturer_id = models.CharField(max_length=5, null=True)
    number_id = models.CharField(max_length=4, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}', writer=ImageWriter)
        # ean = EAN('5901234123457', writer=ImageWriter)
        buffer = BytesIO()
        ean.writer(buffer)
        self.barcode_name.save(f'{self.name}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
