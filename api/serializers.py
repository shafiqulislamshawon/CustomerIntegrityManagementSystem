from rest_framework import serializers
from core.models import *


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class TransactionCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCount
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
