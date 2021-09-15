from django.urls import path
from home import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
