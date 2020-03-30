from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers.ContractSerializer import ContractSerializer
from ..models.ContractModel import Contract
from _datetime import datetime
import json

from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all().order_by('-title')
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]