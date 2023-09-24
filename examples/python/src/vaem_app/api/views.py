from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Status
from .serializer import StatusSerializer

# Create your views here.
class vaem_status_view(APIView):
    def get(self, request):
        # simple pass-through of untranslated status data to get a working example
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
                "access": request.data.get("access"),
                "data_type": request.data.get("data_type"),
                "param_index": request.data.get("param_index"),
                "param_sub_index": request.data.get("param_sub_index"),
                "error_returned": request.data.get("error_returned"),
                "transfer_value": request.data.get("transfer_value"),
                "timestamp": request.data.get("timestamp")
            }

        serializer = StatusSerializer(data=data)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
