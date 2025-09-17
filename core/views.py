from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WeatherView(APIView):
    """Weather endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "Weather endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class WeatherAlertsView(APIView):
    """Weather alerts endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "Weather alerts endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
