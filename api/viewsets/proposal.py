from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models.proposal import Proposal
from _datetime import datetime
import json

from rest_framework import viewsets
from ..serializers.proposal import ProposalSerializer

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all().order_by('name')
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated]