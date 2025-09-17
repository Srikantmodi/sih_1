from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    # Chatbot endpoints
    path('query/', views.ChatbotQueryView.as_view(), name='query'),
    path('sessions/', views.ChatSessionListView.as_view(), name='sessions'),
    path('sessions/<str:session_id>/', views.ChatSessionDetailView.as_view(), name='session-detail'),
]