
#from django.shortcuts import render
#from listviajes_app.models import Viaje
#from django.http import JsonResponse

# Create your views here.

#def viaje_list(request):
#    viaje = Viaje.objects.all()
#    data = {'viaje': list(viaje.values())        
#        }
    
#    return JsonResponse(data)

#def viaje_detalle(request, pk):
#    viaje = Viaje.objects.get(pk=pk)
#    data = {
#        'hora_salida': viaje.hora_salida,
#        'lugarInicio': viaje.lugarInicio, 
#        'lugarDestino': viaje.lugarDestino, 
#        'precio': viaje.precio,        
#        }
#    return JsonResponse(data)
