# Generated by Django 3.1 on 2020-12-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QR_Code_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qrcode_name', models.ImageField(blank=True, upload_to='QR_Code_Images/%Y/%m/%d')),
            ],
        ),
    ]
