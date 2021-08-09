# Generated by Django 3.2.4 on 2021-08-09 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo_img', models.ImageField(upload_to='logo_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.IntegerField(default='')),
                ('adress', models.TextField()),
                ('home_phone', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Employe',
                'verbose_name_plural': 'Employes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'Sub Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(verbose_name='Izoh qoldiring')),
                ('gender', models.CharField(choices=[('man', 'Erkak'), ('woman', 'Ayol'), ('children', 'Bolalar')], default='man', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=200)),
                ('arrive_time', models.DateTimeField(auto_now=True)),
                ('sale_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('shipping_date', models.DateTimeField(auto_now=True)),
                ('shipping_adress', models.TextField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.employes')),
                ('products', models.ManyToManyField(to='shop.Products')),
            ],
        ),
    ]
