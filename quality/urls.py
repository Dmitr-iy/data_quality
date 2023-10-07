from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from quality.views import signup_view

urlpatterns = [
    path('', views.add_concentrate, name='add_concentrate'),
    path('report/', views.report, name='report'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
]
