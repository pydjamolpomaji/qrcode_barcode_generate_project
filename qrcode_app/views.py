from django.shortcuts import render
from .forms import qrcode_form
from django.http import HttpResponseRedirect
from barcode_app.models import Barcode_Model
from qrcode_app.models import QR_Code_Model
from django.contrib import messages


def home_view(request):
    return render(request, 'main.html')


def generated_data(request):
    barcode_data = Barcode_Model.objects.all()
    qrcode_data = QR_Code_Model.objects.all()
    return render(request, 'generated_data.html', {'brdata': barcode_data, 'qrdata': qrcode_data})


def del_qrcode_data(request, id):
    if request.method == 'POST':
        dl = QR_Code_Model.objects.get(pk=id)
        dl.delete()
        messages.warning(request, 'Successfully Deleted you Qrcode...!!')
        return HttpResponseRedirect('/qrcode/generated_data')


def qr_code_view(request):
    if request.method == 'POST':
        form = qrcode_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/qrcode/qrcode_generate_done')
    else:
        form = qrcode_form()
    return render(request, 'qrcode/qrcode.html', {'form': form})


def qrcode_done_view(request):
    return render(request, 'qrcode/qrcode_done.html')
