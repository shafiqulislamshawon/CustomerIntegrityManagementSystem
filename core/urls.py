from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout_request, name="logout")
]
