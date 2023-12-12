from django.http import JsonResponse
from rest_framework.response import Response 
from listviajes_app.models import Viaje
from listviajes_app.api.serializers import ViajeSerializer
from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from listviajes_app.api.permissions import AdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class viaje_create(generics.CreateAPIView):
    permission_classes = [AdminOrReadOnly]
    serializer_class = ViajeSerializer
    def perform_create(self, serializer):
        return super().perform_create(serializer)
        serializer.save()
        
class viaje_list(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViajeSerializer
    def get_queryset(self):
       
       return Viaje.objects.all()
       
class viaje_detalle(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = [AdminOrReadOnly]
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    
    






# @api_view(['GET','POST'])
# def viaje_list(request):
#     if request.method == 'GET':
#         viajes = Viaje.objects.all()
#         serializer = ViajeSerializer(viajes, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         de_serializer = ViajeSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             Response(de_serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def viaje_detalle(request, pk):
#     if request.method == 'GET':
#         try:           
#             viaje = Viaje.objects.get(pk=pk)
#             serializer = ViajeSerializer(viaje)
#             return Response(serializer.data)
#         except Viaje.DoesNotExist:
#             return Response('Error: Viaje no encontrado', status=status.HTTP_404_NOT_FOUND)
    
    
#     if request.method == 'PUT':
#         try: 
#             viaje = Viaje.objects.get(pk=pk)
#             de_serializer = ViajeSerializer(viaje, data=request.data)
        
#             if de_serializer.is_valid():
#                 de_serializer.save()
#                 return Response(de_serializer.data)
#             else:
#                 return Response(de_serializer.errors)
#         except:
#             return Response('Error: Error en el ingreso de datos', status=status.HTTP_400_BAD_REQUEST)
            
#     if request.method == 'DELETE':
#         viaje = Viaje.objects.get(pk=pk)
#         viaje.delete()
#         data = {'message': 'Viaje eliminado'}
#         return Response(data)

