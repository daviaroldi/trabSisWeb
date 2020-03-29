from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models.contract import Contract
from _datetime import datetime
import json

from rest_framework import viewsets
from ..serializers.contract import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all().order_by('-title')
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]