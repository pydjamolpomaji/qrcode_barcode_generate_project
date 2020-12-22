from django.urls import path
from barcode_app import views

app_name = 'barcode_app'
urlpatterns = [
    path('barcode_generate/', views.barcode_view, name='barcode_generate'),
    path('barcode_generate_done/', views.barcode_done_view, name='barcode_generate_done'),
    path('del_barcode_data/<int:id>/', views.del_barcode_data, name='del_barcode_data'),
]
