from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('total-transaction-count/', get_transaction_count.as_view(), name='get_transaction_count'),
    path('get_transaction/', get_transaction.as_view(), name='get_transaction'),

]
