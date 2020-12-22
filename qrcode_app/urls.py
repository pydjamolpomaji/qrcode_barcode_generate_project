from django.urls import path
from qrcode_app import views

app_name = 'qrcode_app'
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('generated_data/', views.generated_data, name='generated_data'),
    path('delete_qrcode_data/<int:id>/', views.del_qrcode_data, name='del_qrcode_data'),
    path('qrcode_generate/', views.qr_code_view, name='qrcode_generate'),
    path('qrcode_generate_done/', views.qrcode_done_view, name='qrcode_done')
]
