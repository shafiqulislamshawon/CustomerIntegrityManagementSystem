from django.urls import path
from .views import *


urlpatterns = [
    path('total-transaction-count/', login_required(get_transaction_count.as_view()), name='get_transaction_count'),
    path('get_transaction/', login_required(get_transaction.as_view()), name='get_transaction'),
]
