from rest_framework import serializers
from listviajes_app.models import Viaje


class ViajeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hora_salida = serializers.CharField()
    lugarInicio = serializers.CharField()
    lugarDestino = serializers.CharField()
    precio = serializers.CharField()
    
    def create(self, validated_data):
        return Viaje.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.hora_salida = validated_data.get('hora_salida', instance.hora_salida)
        instance.lugarInicio = validated_data.get('lugarInicio', instance.lugarInicio)
        instance.lugarDestino = validated_data.get('lugarDestino', instance.lugarDestino)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.save()
        return instance
    