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


class FertilizationRecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FertilizationRecommendation
        fields = (
            'pk', 
            'application_measured_unit', 
            'application_quantity', 
            'substance_contained', 
        )


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Activity
        fields = (
            'pk', 
            'daily_start', 
            'activity', 
            'comment', 
            'percentage_executed', 
            'daily_end', 
            'work_done', 
        )


class AgriculturalProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgriculturalProgramme
        fields = (
            'pk', 
            'comments', 
            'end', 
            'targets', 
            'description', 
            'start', 
            'purpose', 
        )


class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Crop
        fields = (
            'pk', 
            'cultural_name', 
            'monetary_value_per_hectar', 
            'description', 
            'monetary_value_currency', 
            'botanical_name', 
        )


class FieldCultivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FieldCultivation
        fields = (
            'pk', 
            'duration_unit', 
            'duration_of_use', 
        )


class SampleBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SampleBase
        fields = (
            'pk', 
            'source_certificate', 
            'received_time', 
            'concentration', 
            'weight_unit', 
            'recieved_date', 
            'volume', 
            'analysis_date', 
            'comment', 
            'description', 
            'information_source', 
            'volume_unit', 
            'analysis_time', 
            'weight', 
            'composition', 
        )


class SoilSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SoilSample
        fields = (
            'pk', 
            'soil_texture', 
            'analysis_method', 
            'soil_heaviness', 
            'soil_name', 
            'spatial_data', 
            'reference_part_of_field', 
            'soil_nutrient_classification', 
            'depth_range', 
            'soil_type', 
            'depth_unit', 
            'depth', 
        )


class RecordedStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecordedStatus
        fields = (
            'pk', 
            'status_date', 
            'status_time', 
        )


class HarvestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Harvest
        fields = (
            'pk', 
            'quantity_unit', 
            'harvested_quantity', 
            'harvest_quality', 
            'end_date', 
            'yield_quantity', 
            'start_date', 
        )


class AnalysisResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AnalysisResult
        fields = (
            'pk', 
            'parameters', 
            'method', 
            'comment', 
            'description', 
            'abstract_analysis', 
        )


class ProgrammePerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProgrammePerformance
        fields = (
            'pk', 
            'event_coverage', 
            'programme_activities', 
            'comments', 
            'participants', 
            'learning_points', 
            'participant_suggestions', 
            'recommendations', 
        )


class FertilizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fertilizer
        fields = (
            'pk', 
            'fertilizer_type', 
            'fertlizer_name', 
            'fertilizer_brand', 
            'fertilizer_form', 
        )


class FarmFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FarmField
        fields = (
            'pk', 
            'area', 
            'field_identification', 
            'area_unit', 
            'unique_area_id', 
            'name_of_field', 
            'part_of_farm', 
        )


class GenericStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GenericStatus
        fields = (
            'pk', 
            'status_name', 
            'meaning', 
            'staus', 
        )


class CropGrowthStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CropGrowthStage
        fields = (
            'pk', 
            'time_recorded', 
            'growth_stage', 
            'date_recorded', 
            'observer', 
        )


class CropSpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CropSpecies
        fields = (
            'pk', 
            'genetically_modified_organism', 
            'variety', 
            'name', 
        )


class MeasuredKPISerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MeasuredKPI
        fields = (
            'pk', 
            'impact_assessment', 
        )


class LandUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LandUse
        fields = (
            'pk', 
            'land_use_type', 
            'farming_attribute', 
            'land_use_restriction_type', 
            'land_use', 
        )


class ContaminationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contamination
        fields = (
            'pk', 
            'contamination_degree', 
            'noticed_date', 
            'contaimination_type', 
            'noticed_time', 
        )


