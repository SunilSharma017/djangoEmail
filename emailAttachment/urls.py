
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home")
]