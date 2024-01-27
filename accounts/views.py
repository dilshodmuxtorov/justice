from rest_framework import generics
from .models import AccountsModel
from .serializers import AccountSerializer, AccountDetailSerializer

class AccountsView(generics.ListAPIView):
    queryset = AccountsModel.objects.all()
    serializer_class = AccountSerializer

class AccountsDetailView(generics.RetrieveAPIView):
    queryset = AccountsModel.objects.all()
    serializer_class = AccountDetailSerializer
    