from rest_framework.serializers import ModelSerializer
from .models import AccountsModel, HelpModel


class HelpsDetailSerializer(ModelSerializer):
    class Meta:
        model = HelpModel
        fields = "__all__"

class AccountSerializer(ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ['id','name','surname','middlename','birth']

class AccountDetailSerializer(ModelSerializer):
    helps = HelpsDetailSerializer(many=True) 
    class Meta:
        model = AccountsModel
        fields = ['id', 'name', 'surname', 'middlename', 'birth', 'region', 'city', 'helps']
