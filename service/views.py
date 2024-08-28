from django.http import JsonResponse
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from django.db.models import Sum
from rest_framework import viewsets
from .models import Component, Vehicle, Issue, Transaction
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer, TransactionSerializer
from datetime import datetime

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def revenue_data(request):
    today = datetime.now().date()

    daily_revenue = (Transaction.objects
                     .annotate(day=TruncDay('date'))
                     .values('day')
                     .annotate(revenue=Sum('final_price'))
                     .order_by('day'))

    monthly_revenue = (Transaction.objects
                       .annotate(month=TruncMonth('date'))
                       .values('month')
                       .annotate(revenue=Sum('final_price'))
                       .order_by('month'))

    yearly_revenue = (Transaction.objects
                      .annotate(year=TruncYear('date'))
                      .values('year')
                      .annotate(revenue=Sum('final_price'))
                      .order_by('year'))

    response_data = {
        'daily': list(daily_revenue),
        'monthly': list(monthly_revenue),
        'yearly': list(yearly_revenue)
    }

    return JsonResponse(response_data)
