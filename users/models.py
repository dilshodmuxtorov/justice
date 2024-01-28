from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length = 65)
    surname = models.CharField(max_length = 65)
    phone = models.CharField(max_length = 13)
    password = models.CharField(max_length = 65)

    def __str__(self) -> str:
        return self.name
    

