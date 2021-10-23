# mi_web/urls.py
from django.contrib import admin
from django.urls import path
from app.front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat),
]
