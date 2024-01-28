from rest_framework.serializers import ModelSerializer
from .models import ArizaModel

class ArizaModelSerializer(ModelSerializer):
    class Meta:
        model = ArizaModel
        fields = "__all__"