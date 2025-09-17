from django.urls import path
from . import views

app_name = 'farm'

urlpatterns = [
    # Farm profile endpoints
    path('profile/', views.FarmProfileView.as_view(), name='profile'),
    
    # Diary entry endpoints
    path('diary/', views.DiaryEntryListCreateView.as_view(), name='diary-list'),
    path('diary/<int:pk>/', views.DiaryEntryDetailView.as_view(), name='diary-detail'),
]