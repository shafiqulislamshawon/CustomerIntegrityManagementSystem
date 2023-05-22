from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('details/<str:Receiver>/', details, name='details'),

]
