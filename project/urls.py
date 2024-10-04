"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from accaunt.views import (
                        home,detail, about, category, 
                        contact, search,Login,Logout, 
                        detail,createlon, create_image,
                        edit,delete,discount, register
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('Login/', Login , name='login'),
    path('create/', createlon, name='create'),
    path('logout/', Logout, name='logout'), 
    path('detail/<int:id>/', detail, name='detail'),
    path('category/', category, name="category"),
    path('edit/<int:id>/', edit, name='edit'),
    path('create/image/<int:id>/', create_image, name="create_image"),
    path('delete/<int:id>/', delete, name='delete'),
    path('discount/', discount, name='discount'),
    path('register/', register, name='register')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
