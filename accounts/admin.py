from django.contrib import admin
from .models import AccountsModel,HelpModel


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','middlename','birth','region','city')



admin.site.register(AccountsModel,AccountAdmin)
admin.site.register(HelpModel)

