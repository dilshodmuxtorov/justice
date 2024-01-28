from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import UserModel

class UniquePhoneNumberPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        phone = request.data.get('phone', None)

        if phone is not None:
            if UserModel.objects.filter(phone=phone).exists():
                raise PermissionDenied(detail='User with this phone number already exists.')
            else:
                return True
        else:
            return True

# class UserLoginPermission(permissions.BasePermission):


#     def has_permission(self, request, view):
#         phone_number = request.data.get('phone_number', None)
#         password = request.data.get('password', None)

#         if phone_number and password:
#             user = UserModel.objects.filter(phone_number=phone_number).first()

#             if not user:
#                 raise PermissionDenied(detail='Phone number is not registered.')

#             if not user.check_password(password):
#                 raise PermissionDenied(detail='Password is incorrect.')
            
#             request.user = user

#             return True
#         else:
#             raise PermissionDenied(detail='Phone number and password are required in the request.')