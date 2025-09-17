from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    # Financial ledger endpoints
    path('ledger/', views.FinancialLedgerListCreateView.as_view(), name='ledger-list'),
    path('ledger/<int:pk>/', views.FinancialLedgerDetailView.as_view(), name='ledger-detail'),
    path('summary/', views.FinancialSummaryView.as_view(), name='summary'),
]