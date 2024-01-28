from rest_framework import generics ,status
from .models import UserModel
from .serializers import UserModelSerializer
from .permissions import UniquePhoneNumberPermission
from rest_framework.response import Response
from rest_framework.views import APIView



class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (UniquePhoneNumberPermission,)



class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', '')
        password = request.data.get('password', '')

        try:
            user = UserModel.objects.get(phone=phone, password=password)
        except UserModel.DoesNotExist:
            return Response({'error': 'Invalid phone or password'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
