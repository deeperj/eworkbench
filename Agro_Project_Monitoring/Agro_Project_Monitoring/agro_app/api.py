from . import models
from . import serializers
from rest_framework import viewsets, permissions


class CertificationValidityViewSet(viewsets.ModelViewSet):
    """ViewSet for the CertificationValidity class"""

    queryset = models.CertificationValidity.objects.all()
    serializer_class = serializers.CertificationValiditySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgramPerformanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProgramPerformance class"""

    queryset = models.ProgramPerformance.objects.all()
    serializer_class = serializers.ProgramPerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class WeatherViewSet(viewsets.ModelViewSet):
    """ViewSet for the Weather class"""

    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgroDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the AgroDocument class"""

    queryset = models.AgroDocument.objects.all()
    serializer_class = serializers.AgroDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmViewSet(viewsets.ModelViewSet):
    """ViewSet for the Farm class"""

    queryset = models.Farm.objects.all()
    serializer_class = serializers.FarmSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    """ViewSet for the Certificate class"""

    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]


