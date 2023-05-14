from django.db import models


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
    Sender = models.CharField(max_length=100)
    Receiver = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=18, decimal_places=5, null=True, blank=True, default=0)
    TransactionDate = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Suspicious')

    def __str__(self):
        return str(self.TransactionDate)
