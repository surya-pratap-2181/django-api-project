from . import views
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('api/register/', views.RegisterAPI.as_view(), name='apiregister'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/',  knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
