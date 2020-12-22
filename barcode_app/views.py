from django.shortcuts import render
from .forms import BarcodeModelForm
from django.http import HttpResponseRedirect
from .models import Barcode_Model


def barcode_view(request):
    if request.method == 'POST':
        form = BarcodeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/barcode/barcode_generate_done')
    else:
        form = BarcodeModelForm()
    return render(request, 'barcode/barcode.html', {'form': form})


def del_barcode_data(request, id):
    if request.method == 'POST':
        dl = Barcode_Model.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/qrcode/generated_data')


def barcode_done_view(request):
    return render(request, 'barcode/barcode_done.html')
