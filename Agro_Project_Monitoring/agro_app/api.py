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


class FertilizationRecommendationViewSet(viewsets.ModelViewSet):
    """ViewSet for the FertilizationRecommendation class"""

    queryset = models.FertilizationRecommendation.objects.all()
    serializer_class = serializers.FertilizationRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for the Activity class"""

    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class AgriculturalProgrammeViewSet(viewsets.ModelViewSet):
    """ViewSet for the AgriculturalProgramme class"""

    queryset = models.AgriculturalProgramme.objects.all()
    serializer_class = serializers.AgriculturalProgrammeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CropViewSet(viewsets.ModelViewSet):
    """ViewSet for the Crop class"""

    queryset = models.Crop.objects.all()
    serializer_class = serializers.CropSerializer
    permission_classes = [permissions.IsAuthenticated]


class FieldCultivationViewSet(viewsets.ModelViewSet):
    """ViewSet for the FieldCultivation class"""

    queryset = models.FieldCultivation.objects.all()
    serializer_class = serializers.FieldCultivationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SampleBaseViewSet(viewsets.ModelViewSet):
    """ViewSet for the SampleBase class"""

    queryset = models.SampleBase.objects.all()
    serializer_class = serializers.SampleBaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoilSampleViewSet(viewsets.ModelViewSet):
    """ViewSet for the SoilSample class"""

    queryset = models.SoilSample.objects.all()
    serializer_class = serializers.SoilSampleSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecordedStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the RecordedStatus class"""

    queryset = models.RecordedStatus.objects.all()
    serializer_class = serializers.RecordedStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class HarvestViewSet(viewsets.ModelViewSet):
    """ViewSet for the Harvest class"""

    queryset = models.Harvest.objects.all()
    serializer_class = serializers.HarvestSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnalysisResultViewSet(viewsets.ModelViewSet):
    """ViewSet for the AnalysisResult class"""

    queryset = models.AnalysisResult.objects.all()
    serializer_class = serializers.AnalysisResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgrammePerformanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProgrammePerformance class"""

    queryset = models.ProgrammePerformance.objects.all()
    serializer_class = serializers.ProgrammePerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class FertilizerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Fertilizer class"""

    queryset = models.Fertilizer.objects.all()
    serializer_class = serializers.FertilizerSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmFieldViewSet(viewsets.ModelViewSet):
    """ViewSet for the FarmField class"""

    queryset = models.FarmField.objects.all()
    serializer_class = serializers.FarmFieldSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenericStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the GenericStatus class"""

    queryset = models.GenericStatus.objects.all()
    serializer_class = serializers.GenericStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class CropGrowthStageViewSet(viewsets.ModelViewSet):
    """ViewSet for the CropGrowthStage class"""

    queryset = models.CropGrowthStage.objects.all()
    serializer_class = serializers.CropGrowthStageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CropSpeciesViewSet(viewsets.ModelViewSet):
    """ViewSet for the CropSpecies class"""

    queryset = models.CropSpecies.objects.all()
    serializer_class = serializers.CropSpeciesSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeasuredKPIViewSet(viewsets.ModelViewSet):
    """ViewSet for the MeasuredKPI class"""

    queryset = models.MeasuredKPI.objects.all()
    serializer_class = serializers.MeasuredKPISerializer
    permission_classes = [permissions.IsAuthenticated]


class LandUseViewSet(viewsets.ModelViewSet):
    """ViewSet for the LandUse class"""

    queryset = models.LandUse.objects.all()
    serializer_class = serializers.LandUseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContaminationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Contamination class"""

    queryset = models.Contamination.objects.all()
    serializer_class = serializers.ContaminationSerializer
    permission_classes = [permissions.IsAuthenticated]


