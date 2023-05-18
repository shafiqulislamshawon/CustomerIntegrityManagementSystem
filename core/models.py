from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class TransactionCount(models.Model):
    TotalCount = models.IntegerField()
    TransactionDate = models.DateField(null=True)

    def __str__(self):
        return str(self.TransactionDate)


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('Suspicious', 'Suspicious'),
        ('NULL', 'NULL')
    )
    TxCode = models.CharField(max_length=100)
    Sender = models.CharField(max_length=100)
    Receiver = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=18, decimal_places=5, null=True, blank=True, default=0)
    TransactionDate = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Suspicious')

    def __str__(self):
        return str(self.TransactionDate)
