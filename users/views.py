from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationView(APIView):
    """User registration endpoint - placeholder"""
    permission_classes = []
    
    def post(self, request):
        return Response(
            {"message": "User registration endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class UserLoginView(APIView):
    """User login endpoint - placeholder"""
    permission_classes = []
    
    def post(self, request):
        return Response(
            {"message": "User login endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class UserLogoutView(APIView):
    """User logout endpoint - placeholder"""
    
    def post(self, request):
        return Response(
            {"message": "User logout endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class UserProfileView(APIView):
    """User profile endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "User profile endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
