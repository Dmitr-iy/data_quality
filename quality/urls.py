from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from quality.views import signup_view, ConcentrateQualityViewSet

router = DefaultRouter()
router.register(r'concentrate', ConcentrateQualityViewSet)


urlpatterns = [
    path('', views.add_concentrate, name='add_concentrate'),
    path('report/', views.report, name='report'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('api/', include(router.urls)),
]
