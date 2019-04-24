from django import forms
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate, FertilizationRecommendation, Activity, AgriculturalProgramme, Crop, FieldCultivation, SampleBase, SoilSample, RecordedStatus, Harvest, AnalysisResult, ProgrammePerformance, Fertilizer, FarmField, GenericStatus, CropGrowthStage, CropSpecies, MeasuredKPI, LandUse, Contamination


class CertificationValidityForm(forms.ModelForm):
    class Meta:
        model = CertificationValidity
        fields = ['valid_for_purpose', 'farm_purpose', 'issue_date', 'start_date', 'expiry_date']


class ProgramPerformanceForm(forms.ModelForm):
    class Meta:
        model = ProgramPerformance
        fields = ['participants', 'program_activities', 'comments', 'learning_points', 'recommendations', 'participants_suggestions', 'event_coverage']


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['temperature', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity']


class AgroDocumentForm(forms.ModelForm):
    class Meta:
        model = AgroDocument
        fields = '__all__'


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name']


class FertilizationRecommendationForm(forms.ModelForm):
    class Meta:
        model = FertilizationRecommendation
        fields = ['application_measured_unit', 'application_quantity', 'substance_contained']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['daily_start', 'activity', 'comment', 'percentage_executed', 'daily_end', 'work_done']


class AgriculturalProgrammeForm(forms.ModelForm):
    class Meta:
        model = AgriculturalProgramme
        fields = ['comments', 'end', 'targets', 'description', 'start', 'purpose']


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['cultural_name', 'monetary_value_per_hectar', 'description', 'monetary_value_currency', 'botanical_name']


class FieldCultivationForm(forms.ModelForm):
    class Meta:
        model = FieldCultivation
        fields = ['duration_unit', 'duration_of_use']


class SampleBaseForm(forms.ModelForm):
    class Meta:
        model = SampleBase
        fields = ['source_certificate', 'received_time', 'concentration', 'weight_unit', 'recieved_date', 'volume', 'analysis_date', 'comment', 'description', 'information_source', 'volume_unit', 'analysis_time', 'weight', 'composition']


class SoilSampleForm(forms.ModelForm):
    class Meta:
        model = SoilSample
        fields = ['soil_texture', 'analysis_method', 'soil_heaviness', 'soil_name', 'spatial_data', 'reference_part_of_field', 'soil_nutrient_classification', 'depth_range', 'soil_type', 'depth_unit', 'depth']


class RecordedStatusForm(forms.ModelForm):
    class Meta:
        model = RecordedStatus
        fields = ['status_date', 'status_time']


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['quantity_unit', 'harvested_quantity', 'harvest_quality', 'end_date', 'yield_quantity', 'start_date']


class AnalysisResultForm(forms.ModelForm):
    class Meta:
        model = AnalysisResult
        fields = ['parameters', 'method', 'comment', 'description', 'abstract_analysis']


class ProgrammePerformanceForm(forms.ModelForm):
    class Meta:
        model = ProgrammePerformance
        fields = ['event_coverage', 'programme_activities', 'comments', 'participants', 'learning_points', 'participant_suggestions', 'recommendations']


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['fertilizer_type', 'fertlizer_name', 'fertilizer_brand', 'fertilizer_form']


class FarmFieldForm(forms.ModelForm):
    class Meta:
        model = FarmField
        fields = ['area', 'field_identification', 'area_unit', 'unique_area_id', 'name_of_field', 'part_of_farm']


class GenericStatusForm(forms.ModelForm):
    class Meta:
        model = GenericStatus
        fields = ['status_name', 'meaning', 'staus']


class CropGrowthStageForm(forms.ModelForm):
    class Meta:
        model = CropGrowthStage
        fields = ['time_recorded', 'growth_stage', 'date_recorded', 'observer']


class CropSpeciesForm(forms.ModelForm):
    class Meta:
        model = CropSpecies
        fields = ['genetically_modified_organism', 'variety', 'name']


class MeasuredKPIForm(forms.ModelForm):
    class Meta:
        model = MeasuredKPI
        fields = ['impact_assessment']


class LandUseForm(forms.ModelForm):
    class Meta:
        model = LandUse
        fields = ['land_use_type', 'farming_attribute', 'land_use_restriction_type', 'land_use']


class ContaminationForm(forms.ModelForm):
    class Meta:
        model = Contamination
        fields = ['contamination_degree', 'noticed_date', 'contaimination_type', 'noticed_time']


