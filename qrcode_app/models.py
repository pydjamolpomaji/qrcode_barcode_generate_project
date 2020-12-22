from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class QR_Code_Model(models.Model):
    name = models.CharField(max_length=200)
    qrcode_name = models.ImageField(upload_to='QR_Code_Images/%Y/%m/%d', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode_name.save(fname, File(buffer), save=False)
        return super().save(*args, **kwargs)
