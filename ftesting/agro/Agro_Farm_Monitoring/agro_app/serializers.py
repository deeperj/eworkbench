from . import models

from rest_framework import serializers


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Farm
        fields = (
            'pk', 
            'description', 
            'purpose', 
            'farming_system', 
        )


class FarmCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FarmCertificate
        fields = (
            'pk', 
            'first_certificate_date', 
            'certification_agency', 
            'certificate_number', 
            'certification_code', 
            'supporting_documents', 
        )


class CertificationValiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CertificationValidity
        fields = (
            'pk', 
            'valid_for_purpose', 
            'farm_purpose', 
            'issue_date', 
            'expiry_date', 
        )


class FarmFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FarmField
        fields = (
            'pk', 
            'name_of_field', 
            'field_identification', 
            'unique_area_id', 
            'area', 
            'area_unit', 
            'spatial_data', 
        )


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Assessment
        fields = (
            'pk', 
        )


class GenericStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GenericStatus
        fields = (
            'pk', 
            'staus', 
            'status_name', 
            'meaning', 
        )


class RecordedStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecordedStatus
        fields = (
            'pk', 
            'status_date', 
            'status_time', 
        )


class LandUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LandUse
        fields = (
            'pk', 
            'land_use_restriction_type', 
        )


class FertilizationRecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FertilizationRecommendation
        fields = (
            'pk', 
        )


class SampleBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SampleBase
        fields = (
            'pk', 
            'recieved_date', 
            'received_time', 
            'description', 
            'comment', 
            'weight', 
            'weight_unit', 
            'volume', 
            'volume_unit', 
            'analysis_date', 
            'analysis_time', 
        )


class SoilSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SoilSample
        fields = (
            'pk', 
            'soil_name', 
            'soil_type', 
            'reference_part_of_field', 
            'spatial_data', 
            'depth', 
            'depth_unit', 
            'depth_range', 
            'analysis_method', 
            'soil_heaviness', 
            'soil_nutrient_classification', 
            'soil_texture', 
        )


class AnalysisResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AnalysisResult
        fields = (
            'pk', 
            'abstract_analysis', 
            'description', 
            'method', 
            'comment', 
        )


class FertilizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fertilizer
        fields = (
            'pk', 
            'fertilizer_brand', 
            'fertlizer_name', 
            'fertilizer_type', 
            'fertilizer_form', 
        )


class FieldCultivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FieldCultivation
        fields = (
            'pk', 
            'duration_of_use', 
            'duration_unit', 
        )


class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Crop
        fields = (
            'pk', 
            'monetary_value_per_hectar', 
            'monetary_value_currency', 
            'botanical_name', 
        )


class CropGrowthStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CropGrowthStage
        fields = (
            'pk', 
            'growth_stage', 
            'date_recorded', 
            'time_recorded', 
        )


class CropSpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CropSpecies
        fields = (
            'pk', 
            'name', 
            'variety', 
            'genetically_modified_organism', 
        )


class HarvestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Harvest
        fields = (
            'pk', 
            'harvested_quantity', 
            'yield_quantity', 
            'quantity_unit', 
            'harvest_quality', 
            'start_date', 
            'end_date', 
        )


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Activity
        fields = (
            'pk', 
            'daily_start', 
            'daily_end', 
            'activity', 
            'comment', 
            'work_done', 
            'percentage_executed', 
        )


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Weather
        fields = (
            'pk', 
            'temperature', 
            'temperature_unit', 
            'wind_speed', 
            'wind_speed_unit', 
            'humidity', 
            'humidity_unit', 
            'precipitation', 
            'precipitation_unit', 
            'solar_radiation', 
            'solar_radiation_unit', 
            'reported_date', 
            'reported_time', 
            'measured_date', 
            'measured_time', 
        )


class ContaminationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contamination
        fields = (
            'pk', 
            'contaimination_type', 
            'contamination_degree', 
            'noticed_date', 
            'noticed_time', 
            'start', 
            'end', 
            'invitations', 
            'consultants', 
            'purpose', 
            'description', 
            'targets', 
            'comments', 
        )


class ProgrammePerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProgrammePerformance
        fields = (
            'pk', 
            'comments', 
            'learning_points', 
            'recommendations', 
            'participant_suggestions', 
        )


class MeasuredKPISerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MeasuredKPI
        fields = (
            'pk', 
            'measured_kpis', 
            'impact_assessment', 
        )


class AgroDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgroDocument
        fields = (
            'pk', 
            'profile', 
        )


