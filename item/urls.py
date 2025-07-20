# item/urls.py
from django.urls import path
from . import views

app_name = 'item'  # ⭐️ INI YANG PENTING ⭐️

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]