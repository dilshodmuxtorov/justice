# Generated by Django 5.0.1 on 2024-01-27 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_accountsmodel_helps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsmodel',
            name='helps',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.helpmodel'),
        ),
    ]
