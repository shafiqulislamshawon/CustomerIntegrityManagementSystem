from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from api.serializers import TransactionSerializer, TransactionCountSerializer
from core.models import *


class get_transaction_count(LoginRequiredMixin, generics.ListAPIView):
    queryset = TransactionCount.objects.all()
    serializer_class = TransactionCountSerializer


class get_transaction(LoginRequiredMixin, generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
