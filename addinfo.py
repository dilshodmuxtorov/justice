import pandas as pd
import os
import django

def datetime(date:str):
    lst = date.split(".")
    lst = lst[-1::-1]
    date = lst[0]+"-"+lst[1]+"-"+lst[2]
    return date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  
django.setup()

from accounts.models import AccountsModel  



excel_file_path = './informationss.xlsx'

df = pd.read_excel(excel_file_path)


for index, row in df.iterrows():

    lst = row['name'].split(" ")
    name = lst[0]
    surname = lst[1]
    if len(lst) == 4:
        middle = lst[2]+" "+lst[3]
    else:
        middle = lst[2]
    date = datetime(row['birth'])
    AccountsModel.objects.create(
        name=name,
        surname = surname,
        middlename = middle,
        birth=date,
        region = row['region'],
        city = row['city']
        
    )

print("Data added to the database successfully.")
