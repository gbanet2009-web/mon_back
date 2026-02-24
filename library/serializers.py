from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    pdfUrl = serializers.URLField(source='pdf_url')

    class Meta:
        model = Document
        fields = ('id', 'title', 'subject', 'class_level', 'pdf_url', 'pdfUrl', 'price', 'doc_type', 'created_at')
