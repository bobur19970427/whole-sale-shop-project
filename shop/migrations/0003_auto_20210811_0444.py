# Generated by Django 3.2.6 on 2021-08-10 23:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_products_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employes',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='employes',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
