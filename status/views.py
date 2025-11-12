from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialized import StatusSerializer
from .models import Status

# Create your views here.
class StatusAlllistview(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
