from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from django.urls import reverse


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='users/', default='user.png')
    phone = models.CharField(max_length=16)
    adress = models.CharField(max_length=150)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    no_image = models.ImageField(default='no_image.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    # def get_absolute_url(self):
    #     return reverse('detail', args=[self.id])

class ProductImages(models.Model):
    image = models.ImageField(upload_to='productImages/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')

    class Meta:
        verbose_name = 'Mahsulot rasmi'
        verbose_name_plural = 'Mahsulot rasmlari'

class Comment(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comments")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)

    def __str__(self) -> str:
        return self.comment
    

class Registration(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.name
    
class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='discount/')
    discount = models.CharField(max_length=50)


class Like(models.Model):
    user = models.ManyToManyField(MyUser)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='likes')