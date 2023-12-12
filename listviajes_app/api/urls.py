from django.urls import path
from listviajes_app.api.views import viaje_list, viaje_detalle, viaje_create



urlpatterns = [
    path('viaje_list', viaje_list.as_view(), name='viaje_list'),
    path('detalle/<int:pk>', viaje_detalle.as_view(), name='viaje_detalle'),
    path('create/', viaje_create.as_view(), name='viaje_create'),
]
