from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models.document import Document
from _datetime import datetime
import json

from rest_framework import viewsets
from ..serializers.document import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('name')
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]