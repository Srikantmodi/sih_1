from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FarmProfileView(APIView):
    """Farm profile endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "Farm profile GET endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
    
    def put(self, request):
        return Response(
            {"message": "Farm profile PUT endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class DiaryEntryListCreateView(APIView):
    """Diary entry list/create endpoint - placeholder"""
    
    def get(self, request):
        return Response(
            {"message": "Diary entries list endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        return Response(
            {"message": "Diary entry creation endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )


class DiaryEntryDetailView(APIView):
    """Diary entry detail endpoint - placeholder"""
    
    def get(self, request, pk):
        return Response(
            {"message": f"Diary entry {pk} detail endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
    
    def put(self, request, pk):
        return Response(
            {"message": f"Diary entry {pk} update endpoint - coming soon"}, 
            status=status.HTTP_200_OK
        )
    
    def delete(self, request, pk):
        return Response(
            {"message": f"Diary entry {pk} delete endpoint - coming soon"}, 
            status=status.HTTP_204_NO_CONTENT
        )
