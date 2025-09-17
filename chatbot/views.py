from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ChatbotQueryView(APIView):
    """Chatbot query endpoint - placeholder"""
    
    def post(self, request):
        return Response(
            {"message": "Chatbot query endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class ChatSessionListView(APIView):
    """Chat session list endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "Chat sessions list endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class ChatSessionDetailView(APIView):
    """Chat session detail endpoint - placeholder"""
    
    def get(self, request, session_id):
        return Response(
            {"message": f"Chat session {session_id} detail endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
