# Generated by Django 5.0.1 on 2024-01-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accountsmodel_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.TextField()),
            ],
        ),
    ]
