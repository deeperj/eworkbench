from django.contrib import admin
from django import forms
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate, FertilizationRecommendation, Activity, AgriculturalProgramme, Crop, FieldCultivation, SampleBase, SoilSample, RecordedStatus, Harvest, AnalysisResult, ProgrammePerformance, Fertilizer, FarmField, GenericStatus, CropGrowthStage, CropSpecies, MeasuredKPI, LandUse, Contamination

class CertificationValidityAdminForm(forms.ModelForm):

    class Meta:
        model = CertificationValidity
        fields = '__all__'


class CertificationValidityAdmin(admin.ModelAdmin):
    form = CertificationValidityAdminForm
    list_display = ['valid_for_purpose', 'farm_purpose', 'created', 'last_updated', 'issue_date', 'start_date', 'expiry_date']
    readonly_fields = ['valid_for_purpose', 'farm_purpose', 'created', 'last_updated', 'issue_date', 'start_date', 'expiry_date']

admin.site.register(CertificationValidity, CertificationValidityAdmin)


class ProgramPerformanceAdminForm(forms.ModelForm):

    class Meta:
        model = ProgramPerformance
        fields = '__all__'


class ProgramPerformanceAdmin(admin.ModelAdmin):
    form = ProgramPerformanceAdminForm
    list_display = ['participants', 'program_activities', 'created', 'last_updated', 'comments', 'learning_points', 'recommendations', 'participants_suggestions', 'event_coverage']
    readonly_fields = ['participants', 'program_activities', 'created', 'last_updated', 'comments', 'learning_points', 'recommendations', 'participants_suggestions', 'event_coverage']

admin.site.register(ProgramPerformance, ProgramPerformanceAdmin)


class WeatherAdminForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = '__all__'


class WeatherAdmin(admin.ModelAdmin):
    form = WeatherAdminForm
    list_display = ['temperature', 'created', 'last_updated', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity']
    readonly_fields = ['temperature', 'created', 'last_updated', 'temperature_unit', 'wind_speed', 'wind_speed_unit', 'humidity']

admin.site.register(Weather, WeatherAdmin)


class AgroDocumentAdminForm(forms.ModelForm):

    class Meta:
        model = AgroDocument
        fields = '__all__'


class AgroDocumentAdmin(admin.ModelAdmin):
    form = AgroDocumentAdminForm
    list_display = ['created', 'last_updated']
    readonly_fields = ['created', 'last_updated']

admin.site.register(AgroDocument, AgroDocumentAdmin)


class FarmAdminForm(forms.ModelForm):

    class Meta:
        model = Farm
        fields = '__all__'


class FarmAdmin(admin.ModelAdmin):
    form = FarmAdminForm
    list_display = ['name', 'created', 'last_updated']
    readonly_fields = ['name', 'created', 'last_updated']

admin.site.register(Farm, FarmAdmin)


class CertificateAdminForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = '__all__'


class CertificateAdmin(admin.ModelAdmin):
    form = CertificateAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Certificate, CertificateAdmin)


class FertilizationRecommendationAdminForm(forms.ModelForm):

    class Meta:
        model = FertilizationRecommendation
        fields = '__all__'


class FertilizationRecommendationAdmin(admin.ModelAdmin):
    form = FertilizationRecommendationAdminForm
    list_display = ['application_measured_unit', 'application_quantity', 'substance_contained']
    readonly_fields = ['application_measured_unit', 'application_quantity', 'substance_contained']

admin.site.register(FertilizationRecommendation, FertilizationRecommendationAdmin)


class ActivityAdminForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = '__all__'


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityAdminForm
    list_display = ['daily_start', 'activity', 'comment', 'percentage_executed', 'daily_end', 'work_done']
    readonly_fields = ['daily_start', 'activity', 'comment', 'percentage_executed', 'daily_end', 'work_done']

admin.site.register(Activity, ActivityAdmin)


class AgriculturalProgrammeAdminForm(forms.ModelForm):

    class Meta:
        model = AgriculturalProgramme
        fields = '__all__'


class AgriculturalProgrammeAdmin(admin.ModelAdmin):
    form = AgriculturalProgrammeAdminForm
    list_display = ['comments', 'end', 'targets', 'description', 'start', 'purpose']
    readonly_fields = ['comments', 'end', 'targets', 'description', 'start', 'purpose']

admin.site.register(AgriculturalProgramme, AgriculturalProgrammeAdmin)


class CropAdminForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = '__all__'


class CropAdmin(admin.ModelAdmin):
    form = CropAdminForm
    list_display = ['cultural_name', 'monetary_value_per_hectar', 'description', 'monetary_value_currency', 'botanical_name']
    readonly_fields = ['cultural_name', 'monetary_value_per_hectar', 'description', 'monetary_value_currency', 'botanical_name']

admin.site.register(Crop, CropAdmin)


class FieldCultivationAdminForm(forms.ModelForm):

    class Meta:
        model = FieldCultivation
        fields = '__all__'


class FieldCultivationAdmin(admin.ModelAdmin):
    form = FieldCultivationAdminForm
    list_display = ['duration_unit', 'duration_of_use']
    readonly_fields = ['duration_unit', 'duration_of_use']

admin.site.register(FieldCultivation, FieldCultivationAdmin)


class SampleBaseAdminForm(forms.ModelForm):

    class Meta:
        model = SampleBase
        fields = '__all__'


class SampleBaseAdmin(admin.ModelAdmin):
    form = SampleBaseAdminForm
    list_display = ['source_certificate', 'received_time', 'concentration', 'weight_unit', 'recieved_date', 'volume', 'analysis_date', 'comment', 'description', 'information_source', 'volume_unit', 'analysis_time', 'weight', 'composition']
    readonly_fields = ['source_certificate', 'received_time', 'concentration', 'weight_unit', 'recieved_date', 'volume', 'analysis_date', 'comment', 'description', 'information_source', 'volume_unit', 'analysis_time', 'weight', 'composition']

admin.site.register(SampleBase, SampleBaseAdmin)


class SoilSampleAdminForm(forms.ModelForm):

    class Meta:
        model = SoilSample
        fields = '__all__'


class SoilSampleAdmin(admin.ModelAdmin):
    form = SoilSampleAdminForm
    list_display = ['soil_texture', 'analysis_method', 'soil_heaviness', 'soil_name', 'spatial_data', 'reference_part_of_field', 'soil_nutrient_classification', 'depth_range', 'soil_type', 'depth_unit', 'depth']
    readonly_fields = ['soil_texture', 'analysis_method', 'soil_heaviness', 'soil_name', 'spatial_data', 'reference_part_of_field', 'soil_nutrient_classification', 'depth_range', 'soil_type', 'depth_unit', 'depth']

admin.site.register(SoilSample, SoilSampleAdmin)


class RecordedStatusAdminForm(forms.ModelForm):

    class Meta:
        model = RecordedStatus
        fields = '__all__'


class RecordedStatusAdmin(admin.ModelAdmin):
    form = RecordedStatusAdminForm
    list_display = ['status_date', 'status_time']
    readonly_fields = ['status_date', 'status_time']

admin.site.register(RecordedStatus, RecordedStatusAdmin)


class HarvestAdminForm(forms.ModelForm):

    class Meta:
        model = Harvest
        fields = '__all__'


class HarvestAdmin(admin.ModelAdmin):
    form = HarvestAdminForm
    list_display = ['quantity_unit', 'harvested_quantity', 'harvest_quality', 'end_date', 'yield_quantity', 'start_date']
    readonly_fields = ['quantity_unit', 'harvested_quantity', 'harvest_quality', 'end_date', 'yield_quantity', 'start_date']

admin.site.register(Harvest, HarvestAdmin)


class AnalysisResultAdminForm(forms.ModelForm):

    class Meta:
        model = AnalysisResult
        fields = '__all__'


class AnalysisResultAdmin(admin.ModelAdmin):
    form = AnalysisResultAdminForm
    list_display = ['parameters', 'method', 'comment', 'description', 'abstract_analysis']
    readonly_fields = ['parameters', 'method', 'comment', 'description', 'abstract_analysis']

admin.site.register(AnalysisResult, AnalysisResultAdmin)


class ProgrammePerformanceAdminForm(forms.ModelForm):

    class Meta:
        model = ProgrammePerformance
        fields = '__all__'


class ProgrammePerformanceAdmin(admin.ModelAdmin):
    form = ProgrammePerformanceAdminForm
    list_display = ['event_coverage', 'programme_activities', 'comments', 'participants', 'learning_points', 'participant_suggestions', 'recommendations']
    readonly_fields = ['event_coverage', 'programme_activities', 'comments', 'participants', 'learning_points', 'participant_suggestions', 'recommendations']

admin.site.register(ProgrammePerformance, ProgrammePerformanceAdmin)


class FertilizerAdminForm(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'


class FertilizerAdmin(admin.ModelAdmin):
    form = FertilizerAdminForm
    list_display = ['fertilizer_type', 'fertlizer_name', 'fertilizer_brand', 'fertilizer_form']
    readonly_fields = ['fertilizer_type', 'fertlizer_name', 'fertilizer_brand', 'fertilizer_form']

admin.site.register(Fertilizer, FertilizerAdmin)


class FarmFieldAdminForm(forms.ModelForm):

    class Meta:
        model = FarmField
        fields = '__all__'


class FarmFieldAdmin(admin.ModelAdmin):
    form = FarmFieldAdminForm
    list_display = ['area', 'field_identification', 'area_unit', 'unique_area_id', 'name_of_field', 'part_of_farm']
    readonly_fields = ['area', 'field_identification', 'area_unit', 'unique_area_id', 'name_of_field', 'part_of_farm']

admin.site.register(FarmField, FarmFieldAdmin)


class GenericStatusAdminForm(forms.ModelForm):

    class Meta:
        model = GenericStatus
        fields = '__all__'


class GenericStatusAdmin(admin.ModelAdmin):
    form = GenericStatusAdminForm
    list_display = ['status_name', 'meaning', 'staus']
    readonly_fields = ['status_name', 'meaning', 'staus']

admin.site.register(GenericStatus, GenericStatusAdmin)


class CropGrowthStageAdminForm(forms.ModelForm):

    class Meta:
        model = CropGrowthStage
        fields = '__all__'


class CropGrowthStageAdmin(admin.ModelAdmin):
    form = CropGrowthStageAdminForm
    list_display = ['time_recorded', 'growth_stage', 'date_recorded', 'observer']
    readonly_fields = ['time_recorded', 'growth_stage', 'date_recorded', 'observer']

admin.site.register(CropGrowthStage, CropGrowthStageAdmin)


class CropSpeciesAdminForm(forms.ModelForm):

    class Meta:
        model = CropSpecies
        fields = '__all__'


class CropSpeciesAdmin(admin.ModelAdmin):
    form = CropSpeciesAdminForm
    list_display = ['genetically_modified_organism', 'variety', 'name']
    readonly_fields = ['genetically_modified_organism', 'variety', 'name']

admin.site.register(CropSpecies, CropSpeciesAdmin)


class MeasuredKPIAdminForm(forms.ModelForm):

    class Meta:
        model = MeasuredKPI
        fields = '__all__'


class MeasuredKPIAdmin(admin.ModelAdmin):
    form = MeasuredKPIAdminForm
    list_display = ['impact_assessment']
    readonly_fields = ['impact_assessment']

admin.site.register(MeasuredKPI, MeasuredKPIAdmin)


class LandUseAdminForm(forms.ModelForm):

    class Meta:
        model = LandUse
        fields = '__all__'


class LandUseAdmin(admin.ModelAdmin):
    form = LandUseAdminForm
    list_display = ['land_use_type', 'farming_attribute', 'land_use_restriction_type', 'land_use']
    readonly_fields = ['land_use_type', 'farming_attribute', 'land_use_restriction_type', 'land_use']

admin.site.register(LandUse, LandUseAdmin)


class ContaminationAdminForm(forms.ModelForm):

    class Meta:
        model = Contamination
        fields = '__all__'


class ContaminationAdmin(admin.ModelAdmin):
    form = ContaminationAdminForm
    list_display = ['contamination_degree', 'noticed_date', 'contaimination_type', 'noticed_time']
    readonly_fields = ['contamination_degree', 'noticed_date', 'contaimination_type', 'noticed_time']

admin.site.register(Contamination, ContaminationAdmin)


