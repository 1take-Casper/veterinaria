from rest_framework import serializers
from .models import Mascota

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = "__all__"