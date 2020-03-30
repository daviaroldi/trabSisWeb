from rest_framework import serializers
from ..models.DocumentModel import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'