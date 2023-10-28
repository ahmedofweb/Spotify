from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from.models import *

class QoshiqchiSerializer(serializers.Serializer):
    class Meta:
        model = Qoshiqchi
        fields = "__all__"

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = "__all__"
    def validate_fayl(self, qiymat):
        if ".mp3" in str(qiymat):
            return qiymat
        raise ValidationError("You need to add only mp3 format of music")
    def validate_davomiylik(self, qiymat):
        if qiymat < 7:
            return qiymat
        raise ValidationError("You have to add your music's continuity less than 7")

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"

    def to_representation(self, instance):
        albom = super(AlbomSerializer, self).to_representation(instance)
        son = Izoh.objects.filter(albom=instance).count()
        albom.update({"izoh_soni": son})
        return albom


class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = "__all__"

