from django import forms
from .models import Farm, FarmCertificate, CertificationValidity, FarmField, Assessment, GenericStatus, RecordedStatus, LandUse, FertilizationRecommendation, SampleBase, SoilSample, AnalysisResult, Fertilizer, FieldCultivation, Crop, CropGrowthStage, CropSpecies, Harvest, Activity, Weather, Contamination, ProgrammePerformance, MeasuredKPI, AgroDocument


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['description', 'purpose', 'farming_system', 'owner']


class FarmCertificateForm(forms.ModelForm):
    class Meta:
        model = FarmCertificate
        fields = ['first_certificate_date', 'certification_agency', 'certificate_number', 'certification_code', 'supporting_documents']


class CertificationValidityForm(forms.ModelForm):
    class Meta:
        model = CertificationValidity
        fields = ['valid_for_purpose', 'farm_purpose', 'issue_date', 'expiry_date']


class FarmFieldForm(forms.ModelForm):
    class Meta:
        model = FarmField
        fields = ['name_of_field', 'field_identification', 'unique_area_id', 'area', 'area_unit', 'spatial_data', 'cultivation', 'land_use_restriction', 'assessment']


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['analysis', 'status']


class GenericStatusForm(forms.ModelForm):
    class Meta:
        model = GenericStatus
        fields = ['staus', 'status_name', 'meaning']


class RecordedStatusForm(forms.ModelForm):
    class Meta:
        model = RecordedStatus
        fields = ['status_date', 'status_time', 'status']


class LandUseForm(forms.ModelForm):
    class Meta:
        model = LandUse
        fields = ['land_use_restriction_type']


class FertilizationRecommendationForm(forms.ModelForm):
    class Meta:
        model = FertilizationRecommendation
        fields = '__all__'


class SampleBaseForm(forms.ModelForm):
    class Meta:
        model = SampleBase
        fields = ['recieved_date', 'received_time', 'description', 'comment', 'weight', 'weight_unit', 'volume', 'volume_unit', 'analysis_date', 'analysis_time']


class SoilSampleForm(forms.ModelForm):
    class Meta:
        model = SoilSample
        fields = ['soil_name', 'soil_type', 'reference_part_of_field', 'spatial_data', 'depth', 'depth_unit', 'depth_range', 'analysis_method', 'soil_heaviness', 'soil_nutrient_classification', 'soil_texture']


class AnalysisResultForm(forms.ModelForm):
    class Meta:
        model = AnalysisResult
        fields = ['abstract_analysis', 'description', 'method', 'comment', 'sample']


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['fertilizer_brand', 'fertlizer_name', 'fertilizer_type', 'fertilizer_form']


class FieldCultivationForm(forms.ModelForm):
    class Meta:
        model = FieldCultivation
        fields = ['duration_of_use', 'duration_unit', 'farm_field', 'reference_field_part']


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['monetary_value_per_hectar', 'monetary_value_currency', 'botanical_name', 'farm_field', 'crop_growth_event']


class CropGrowthStageForm(forms.ModelForm):
    class Meta:
        model = CropGrowthStage
        fields = ['growth_stage', 'date_recorded', 'time_recorded']


class CropSpeciesForm(forms.ModelForm):
    class Meta:
        model = CropSpecies
        fields = ['name', 'variety', 'genetically_modified_organism', 'crop']


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['harvested_quantity', 'yield_quantity', 'quantity_unit', 'harvest_quality', 'start_date', 'end_date', 'crop', 'farm_field']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['daily_start', 'daily_end', 'activity', 'comment', 'work_done', 'percentage_executed']


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['temperature', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity', 'humidity_unit', 'precipitation', 'precipitation_unit', 'solar_radiation', 'solar_radiation_unit', 'reported_date', 'reported_time', 'measured_date', 'measured_time', 'reported_by', 'measured_by']


class ContaminationForm(forms.ModelForm):
    class Meta:
        model = Contamination
        fields = ['contaimination_type', 'contamination_degree', 'noticed_date', 'noticed_time', 'start', 'end', 'invitations', 'consultants', 'purpose', 'description', 'targets', 'comments', 'reported_by', 'affected_fields', 'kpis', 'status']


class ProgrammePerformanceForm(forms.ModelForm):
    class Meta:
        model = ProgrammePerformance
        fields = ['comments', 'learning_points', 'recommendations', 'participant_suggestions']


class MeasuredKPIForm(forms.ModelForm):
    class Meta:
        model = MeasuredKPI
        fields = ['measured_kpis', 'impact_assessment', 'programme_performance', 'fertilizer']


class AgroDocumentForm(forms.ModelForm):
    class Meta:
        model = AgroDocument
        fields = ['profile', 'farm', 'work_process']


