from django.db import models

class HelpModel(models.Model):
    title = models.CharField(max_length = 65)
    description = models.TextField()
   
    def __str__(self) -> str:
        return self.title

class AccountsModel(models.Model):
    name = models.CharField(default = "")
    surname = models.CharField(default = "")
    middlename = models.CharField(default = "")
    birth = models.DateField()
    region = models.CharField(default = "")
    city = models.CharField(default = "")
    helps = models.ManyToManyField(HelpModel, null = True, blank = True, default = None)
    
    
    def __str__(self) -> str:
        return self.name +" " +self.surname


