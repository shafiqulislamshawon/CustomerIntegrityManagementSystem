import requests
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import render, get_object_or_404
import datetime as dt
from core.models import Transaction, TransactionCount


@login_required
def dashboard(request):
    date = dt.date.today() - dt.timedelta(days=1)
    startDate = dt.date.today() - dt.timedelta(days=7)
    endDate = date
    tx = Transaction.objects.filter(TransactionDate__range=[startDate, endDate]).values('Receiver',
                                                                                        'TransactionDate',
                                                                                        'status').annotate(
        Unique_Receiver=Count('Receiver', distinct=True), total_transaction=Count('TxCode'),
        total_Amount=Sum('Amount')).order_by('-TransactionDate')
    total_tx = TransactionCount.objects.filter(TransactionDate__range=[startDate, endDate]).values('TotalCount').annotate(total=Sum('TotalCount'))
    print(total_tx)
    data = [
        {"label": "Category 1", "value": 70},
        {"label": "Category 2", "value": 30},
    ]

    context = {
        'data': data,
        'date': date,
        'startDate': startDate,
        'endDate': endDate,
        'tx': tx,
        'total_tx': total_tx,
    }
    return render(request, 'pages/dashboard.html', context)


@login_required
def details(request, Receiver):
    date = dt.date.today() - dt.timedelta(days=1)
    startDate = dt.date.today() - dt.timedelta(days=7)
    endDate = date
    details = Transaction.objects.filter(TransactionDate__range=[startDate, endDate], Receiver=Receiver)
    details = Transaction.objects.filter(TransactionDate__range=details)
    print(details)
    context = {
        'date': date,
        'startDate': startDate,
        'endDate': endDate,
        'details': details,
    }
    return render(request, 'pages/details.html', context)
