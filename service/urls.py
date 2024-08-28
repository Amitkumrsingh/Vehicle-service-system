from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComponentViewSet, VehicleViewSet, IssueViewSet, TransactionViewSet, revenue_data

router = DefaultRouter()
router.register(r'components', ComponentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('revenue-data/', revenue_data),
]
