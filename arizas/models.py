from django.db import models
from users.models import UserModel

class  ArizaModel(models.Model):
    user_id = models.ForeignKey(UserModel,on_delete = models.CASCADE)
    title = models.CharField(max_length = 65)
    description = models.TextField()
    checkstatus = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.title
