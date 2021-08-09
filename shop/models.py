from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'SubCategory'
        verbose_name_plural = 'Sub Categories'

class Brand(models.Model):
    name = models.CharField(max_length=200)
    logo_img = models.ImageField(upload_to='logo_img/')
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField('Izoh qoldiring')
    GENDER_CHOICES = [
        ('man' , 'Erkak'),
        ('woman', 'Ayol'),
        ('children', 'Bolalar'),

    ]
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default='man')
    image = models.ImageField(upload_to='products/')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200)
    arrive_time = models.DateTimeField(auto_now=True)
    sale_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Employes(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField(default='')
    adress = models.TextField()
    home_phone = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Employe'
        verbose_name_plural = 'Employes'

    def __str__(self):
        return self.name


class Customers(models.Model):
    username = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField(default='')

    class Meta:
        ordering = ('username',)
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.username


class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employes, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    shipping_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Products)
    shipping_adress = models.TextField()

    def __str__(self):
        return self.customer
