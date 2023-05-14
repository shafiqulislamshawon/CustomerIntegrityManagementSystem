from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import TransactionSerializer, TransactionCountSerializer
from core.models import *


class get_transaction_count(generics.ListAPIView):
    queryset = TransactionCount.objects.all()
    serializer_class = TransactionCountSerializer

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})


class get_transaction(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})
