from django.shortcuts import render
from rest_framework import viewsets
from DATA_APP.models import Test
from DATA_APP.serializers import TestSerializer

# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer