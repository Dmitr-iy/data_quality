from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_concentrate, name='add_concentrate'),
]
