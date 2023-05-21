import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime as dt
from core.models import Transaction


@login_required
def dashboard(request):
    date = dt.date.today() - dt.timedelta(days=1)
    startDate = dt.date.today() - dt.timedelta(days=7)
    endDate = date
    tx = Transaction.objects.filter(TransactionDate__range=[startDate, endDate])
    context = {
        'date': date,
        'startDate': startDate,
        'endDate': endDate,
        'tx': tx,
    }
    return render(request, 'pages/dashboard.html', context)
