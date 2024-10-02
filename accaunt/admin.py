from django.contrib import admin
from .models import Category, Product, ProductImages, MyUser, Comment, Registration


admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Product)
admin.site.register(MyUser)
admin.site.register(Comment)
admin.site.register(Registration)
# Register your models here.
