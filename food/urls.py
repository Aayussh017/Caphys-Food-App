"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # /food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # view items
    path('item/', views.item, name='item'),
    # add items 
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # edit 
    path('update/<int:id>/',views.update_item , name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item , name='delete_item'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
