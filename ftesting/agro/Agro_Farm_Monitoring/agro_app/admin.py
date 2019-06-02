from django.contrib import admin
from django import forms
from .models import Farm, FarmCertificate, CertificationValidity, FarmField, Assessment, GenericStatus, RecordedStatus, LandUse, FertilizationRecommendation, SampleBase, SoilSample, AnalysisResult, Fertilizer, FieldCultivation, Crop, CropGrowthStage, CropSpecies, Harvest, Activity, Weather, Contamination, ProgrammePerformance, MeasuredKPI, AgroDocument

class FarmAdminForm(forms.ModelForm):

    class Meta:
        model = Farm
        fields = '__all__'


class FarmAdmin(admin.ModelAdmin):
    form = FarmAdminForm
    list_display = ['description', 'purpose', 'farming_system']
    readonly_fields = ['description', 'purpose', 'farming_system']

admin.site.register(Farm, FarmAdmin)


class FarmCertificateAdminForm(forms.ModelForm):

    class Meta:
        model = FarmCertificate
        fields = '__all__'


class FarmCertificateAdmin(admin.ModelAdmin):
    form = FarmCertificateAdminForm
    list_display = ['first_certificate_date', 'certification_agency', 'certificate_number', 'certification_code', 'supporting_documents']
    readonly_fields = ['first_certificate_date', 'certification_agency', 'certificate_number', 'certification_code', 'supporting_documents']

admin.site.register(FarmCertificate, FarmCertificateAdmin)


class CertificationValidityAdminForm(forms.ModelForm):

    class Meta:
        model = CertificationValidity
        fields = '__all__'


class CertificationValidityAdmin(admin.ModelAdmin):
    form = CertificationValidityAdminForm
    list_display = ['valid_for_purpose', 'farm_purpose', 'issue_date', 'expiry_date']
    readonly_fields = ['valid_for_purpose', 'farm_purpose', 'issue_date', 'expiry_date']

admin.site.register(CertificationValidity, CertificationValidityAdmin)


class FarmFieldAdminForm(forms.ModelForm):

    class Meta:
        model = FarmField
        fields = '__all__'


class FarmFieldAdmin(admin.ModelAdmin):
    form = FarmFieldAdminForm
    list_display = ['name_of_field', 'field_identification', 'unique_area_id', 'area', 'area_unit', 'spatial_data']
    readonly_fields = ['name_of_field', 'field_identification', 'unique_area_id', 'area', 'area_unit', 'spatial_data']

admin.site.register(FarmField, FarmFieldAdmin)


class AssessmentAdminForm(forms.ModelForm):

    class Meta:
        model = Assessment
        fields = '__all__'


class AssessmentAdmin(admin.ModelAdmin):
    form = AssessmentAdminForm


admin.site.register(Assessment, AssessmentAdmin)


class GenericStatusAdminForm(forms.ModelForm):

    class Meta:
        model = GenericStatus
        fields = '__all__'


class GenericStatusAdmin(admin.ModelAdmin):
    form = GenericStatusAdminForm
    list_display = ['staus', 'status_name', 'meaning']
    readonly_fields = ['staus', 'status_name', 'meaning']

admin.site.register(GenericStatus, GenericStatusAdmin)


class RecordedStatusAdminForm(forms.ModelForm):

    class Meta:
        model = RecordedStatus
        fields = '__all__'


class RecordedStatusAdmin(admin.ModelAdmin):
    form = RecordedStatusAdminForm
    list_display = ['status_date', 'status_time']
    readonly_fields = ['status_date', 'status_time']

admin.site.register(RecordedStatus, RecordedStatusAdmin)


class LandUseAdminForm(forms.ModelForm):

    class Meta:
        model = LandUse
        fields = '__all__'


class LandUseAdmin(admin.ModelAdmin):
    form = LandUseAdminForm
    list_display = ['land_use_restriction_type']
    readonly_fields = ['land_use_restriction_type']

admin.site.register(LandUse, LandUseAdmin)


class FertilizationRecommendationAdminForm(forms.ModelForm):

    class Meta:
        model = FertilizationRecommendation
        fields = '__all__'


class FertilizationRecommendationAdmin(admin.ModelAdmin):
    form = FertilizationRecommendationAdminForm


admin.site.register(FertilizationRecommendation, FertilizationRecommendationAdmin)


class SampleBaseAdminForm(forms.ModelForm):

    class Meta:
        model = SampleBase
        fields = '__all__'


class SampleBaseAdmin(admin.ModelAdmin):
    form = SampleBaseAdminForm
    list_display = ['recieved_date', 'received_time', 'description', 'comment', 'weight', 'weight_unit', 'volume', 'volume_unit', 'analysis_date', 'analysis_time']
    readonly_fields = ['recieved_date', 'received_time', 'description', 'comment', 'weight', 'weight_unit', 'volume', 'volume_unit', 'analysis_date', 'analysis_time']

admin.site.register(SampleBase, SampleBaseAdmin)


class SoilSampleAdminForm(forms.ModelForm):

    class Meta:
        model = SoilSample
        fields = '__all__'


class SoilSampleAdmin(admin.ModelAdmin):
    form = SoilSampleAdminForm
    list_display = ['soil_name', 'soil_type', 'reference_part_of_field', 'spatial_data', 'depth', 'depth_unit', 'depth_range', 'analysis_method', 'soil_heaviness', 'soil_nutrient_classification', 'soil_texture']
    readonly_fields = ['soil_name', 'soil_type', 'reference_part_of_field', 'spatial_data', 'depth', 'depth_unit', 'depth_range', 'analysis_method', 'soil_heaviness', 'soil_nutrient_classification', 'soil_texture']

admin.site.register(SoilSample, SoilSampleAdmin)


class AnalysisResultAdminForm(forms.ModelForm):

    class Meta:
        model = AnalysisResult
        fields = '__all__'


class AnalysisResultAdmin(admin.ModelAdmin):
    form = AnalysisResultAdminForm
    list_display = ['abstract_analysis', 'description', 'method', 'comment']
    readonly_fields = ['abstract_analysis', 'description', 'method', 'comment']

admin.site.register(AnalysisResult, AnalysisResultAdmin)


class FertilizerAdminForm(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'


class FertilizerAdmin(admin.ModelAdmin):
    form = FertilizerAdminForm
    list_display = ['fertilizer_brand', 'fertlizer_name', 'fertilizer_type', 'fertilizer_form']
    readonly_fields = ['fertilizer_brand', 'fertlizer_name', 'fertilizer_type', 'fertilizer_form']

admin.site.register(Fertilizer, FertilizerAdmin)


class FieldCultivationAdminForm(forms.ModelForm):

    class Meta:
        model = FieldCultivation
        fields = '__all__'


class FieldCultivationAdmin(admin.ModelAdmin):
    form = FieldCultivationAdminForm
    list_display = ['duration_of_use', 'duration_unit']
    readonly_fields = ['duration_of_use', 'duration_unit']

admin.site.register(FieldCultivation, FieldCultivationAdmin)


class CropAdminForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = '__all__'


class CropAdmin(admin.ModelAdmin):
    form = CropAdminForm
    list_display = ['monetary_value_per_hectar', 'monetary_value_currency', 'botanical_name']
    readonly_fields = ['monetary_value_per_hectar', 'monetary_value_currency', 'botanical_name']

admin.site.register(Crop, CropAdmin)


class CropGrowthStageAdminForm(forms.ModelForm):

    class Meta:
        model = CropGrowthStage
        fields = '__all__'


class CropGrowthStageAdmin(admin.ModelAdmin):
    form = CropGrowthStageAdminForm
    list_display = ['growth_stage', 'date_recorded', 'time_recorded']
    readonly_fields = ['growth_stage', 'date_recorded', 'time_recorded']

admin.site.register(CropGrowthStage, CropGrowthStageAdmin)


class CropSpeciesAdminForm(forms.ModelForm):

    class Meta:
        model = CropSpecies
        fields = '__all__'


class CropSpeciesAdmin(admin.ModelAdmin):
    form = CropSpeciesAdminForm
    list_display = ['name', 'variety', 'genetically_modified_organism']
    readonly_fields = ['name', 'variety', 'genetically_modified_organism']

admin.site.register(CropSpecies, CropSpeciesAdmin)


class HarvestAdminForm(forms.ModelForm):

    class Meta:
        model = Harvest
        fields = '__all__'


class HarvestAdmin(admin.ModelAdmin):
    form = HarvestAdminForm
    list_display = ['harvested_quantity', 'yield_quantity', 'quantity_unit', 'harvest_quality', 'start_date', 'end_date']
    readonly_fields = ['harvested_quantity', 'yield_quantity', 'quantity_unit', 'harvest_quality', 'start_date', 'end_date']

admin.site.register(Harvest, HarvestAdmin)


class ActivityAdminForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = '__all__'


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityAdminForm
    list_display = ['daily_start', 'daily_end', 'activity', 'comment', 'work_done', 'percentage_executed']
    readonly_fields = ['daily_start', 'daily_end', 'activity', 'comment', 'work_done', 'percentage_executed']

admin.site.register(Activity, ActivityAdmin)


class WeatherAdminForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = '__all__'


class WeatherAdmin(admin.ModelAdmin):
    form = WeatherAdminForm
    list_display = ['temperature', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity', 'humidity_unit', 'precipitation', 'precipitation_unit', 'solar_radiation', 'solar_radiation_unit', 'reported_date', 'reported_time', 'measured_date', 'measured_time']
    readonly_fields = ['temperature', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity', 'humidity_unit', 'precipitation', 'precipitation_unit', 'solar_radiation', 'solar_radiation_unit', 'reported_date', 'reported_time', 'measured_date', 'measured_time']

admin.site.register(Weather, WeatherAdmin)


class ContaminationAdminForm(forms.ModelForm):

    class Meta:
        model = Contamination
        fields = '__all__'


class ContaminationAdmin(admin.ModelAdmin):
    form = ContaminationAdminForm
    list_display = ['contaimination_type', 'contamination_degree', 'noticed_date', 'noticed_time', 'start', 'end', 'invitations', 'consultants', 'purpose', 'description', 'targets', 'comments']
    readonly_fields = ['contaimination_type', 'contamination_degree', 'noticed_date', 'noticed_time', 'start', 'end', 'invitations', 'consultants', 'purpose', 'description', 'targets', 'comments']

admin.site.register(Contamination, ContaminationAdmin)


class ProgrammePerformanceAdminForm(forms.ModelForm):

    class Meta:
        model = ProgrammePerformance
        fields = '__all__'


class ProgrammePerformanceAdmin(admin.ModelAdmin):
    form = ProgrammePerformanceAdminForm
    list_display = ['comments', 'learning_points', 'recommendations', 'participant_suggestions']
    readonly_fields = ['comments', 'learning_points', 'recommendations', 'participant_suggestions']

admin.site.register(ProgrammePerformance, ProgrammePerformanceAdmin)


class MeasuredKPIAdminForm(forms.ModelForm):

    class Meta:
        model = MeasuredKPI
        fields = '__all__'


class MeasuredKPIAdmin(admin.ModelAdmin):
    form = MeasuredKPIAdminForm
    list_display = ['measured_kpis', 'impact_assessment']
    readonly_fields = ['measured_kpis', 'impact_assessment']

admin.site.register(MeasuredKPI, MeasuredKPIAdmin)


class AgroDocumentAdminForm(forms.ModelForm):

    class Meta:
        model = AgroDocument
        fields = '__all__'


class AgroDocumentAdmin(admin.ModelAdmin):
    form = AgroDocumentAdminForm
    list_display = ['profile']
    readonly_fields = ['profile']

admin.site.register(AgroDocument, AgroDocumentAdmin)


