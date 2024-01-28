from rest_framework import generics
from .models import ArizaModel
from .serializers import ArizaModelSerializer
from .permissions import IsOwnerOrReadOnly

class ArizaList(generics.ListAPIView):
    queryset = ArizaModel.objects.all()
    serializer_class = ArizaModelSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    
    
class ArizaCreateView(generics.CreateAPIView):
    queryset = ArizaModel.objects.all()
    serializer_class = ArizaModelSerializer

