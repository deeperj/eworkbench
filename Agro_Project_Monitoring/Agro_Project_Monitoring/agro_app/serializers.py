from . import models

from rest_framework import serializers


class CertificationValiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CertificationValidity
        fields = (
            'pk', 
            'valid_for_purpose', 
            'farm_purpose', 
            'created', 
            'last_updated', 
            'issue_date', 
            'start_date', 
            'expiry_date', 
        )


class ProgramPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProgramPerformance
        fields = (
            'pk', 
            'participants', 
            'program_activities', 
            'created', 
            'last_updated', 
            'comments', 
            'learning_points', 
            'recommendations', 
            'participants_suggestions', 
            'event_coverage', 
        )


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Weather
        fields = (
            'pk', 
            'temperature', 
            'created', 
            'last_updated', 
            'temperature_unit', 
            'wind_speed', 
            'wind_speed_unit', 
            'humidity', 
        )


class AgroDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgroDocument
        fields = (
            'pk', 
            'created', 
            'last_updated', 
        )


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Farm
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Certificate
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


