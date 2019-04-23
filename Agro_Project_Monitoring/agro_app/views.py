from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate, FertilizationRecommendation, Activity, AgriculturalProgramme, Crop, FieldCultivation, SampleBase, SoilSample, RecordedStatus, Harvest, AnalysisResult, ProgrammePerformance, Fertilizer, FarmField, GenericStatus, CropGrowthStage, CropSpecies, MeasuredKPI, LandUse, Contamination
from .forms import CertificationValidityForm, ProgramPerformanceForm, WeatherForm, AgroDocumentForm, FarmForm, CertificateForm, FertilizationRecommendationForm, ActivityForm, AgriculturalProgrammeForm, CropForm, FieldCultivationForm, SampleBaseForm, SoilSampleForm, RecordedStatusForm, HarvestForm, AnalysisResultForm, ProgrammePerformanceForm, FertilizerForm, FarmFieldForm, GenericStatusForm, CropGrowthStageForm, CropSpeciesForm, MeasuredKPIForm, LandUseForm, ContaminationForm


class CertificationValidityListView(ListView):
    model = CertificationValidity


class CertificationValidityCreateView(CreateView):
    model = CertificationValidity
    form_class = CertificationValidityForm


class CertificationValidityDetailView(DetailView):
    model = CertificationValidity


class CertificationValidityUpdateView(UpdateView):
    model = CertificationValidity
    form_class = CertificationValidityForm


class ProgramPerformanceListView(ListView):
    model = ProgramPerformance


class ProgramPerformanceCreateView(CreateView):
    model = ProgramPerformance
    form_class = ProgramPerformanceForm


class ProgramPerformanceDetailView(DetailView):
    model = ProgramPerformance


class ProgramPerformanceUpdateView(UpdateView):
    model = ProgramPerformance
    form_class = ProgramPerformanceForm


class WeatherListView(ListView):
    model = Weather


class WeatherCreateView(CreateView):
    model = Weather
    form_class = WeatherForm


class WeatherDetailView(DetailView):
    model = Weather


class WeatherUpdateView(UpdateView):
    model = Weather
    form_class = WeatherForm


class AgroDocumentListView(ListView):
    model = AgroDocument


class AgroDocumentCreateView(CreateView):
    model = AgroDocument
    form_class = AgroDocumentForm


class AgroDocumentDetailView(DetailView):
    model = AgroDocument


class AgroDocumentUpdateView(UpdateView):
    model = AgroDocument
    form_class = AgroDocumentForm


class FarmListView(ListView):
    model = Farm


class FarmCreateView(CreateView):
    model = Farm
    form_class = FarmForm


class FarmDetailView(DetailView):
    model = Farm


class FarmUpdateView(UpdateView):
    model = Farm
    form_class = FarmForm


class CertificateListView(ListView):
    model = Certificate


class CertificateCreateView(CreateView):
    model = Certificate
    form_class = CertificateForm


class CertificateDetailView(DetailView):
    model = Certificate


class CertificateUpdateView(UpdateView):
    model = Certificate
    form_class = CertificateForm


class FertilizationRecommendationListView(ListView):
    model = FertilizationRecommendation


class FertilizationRecommendationCreateView(CreateView):
    model = FertilizationRecommendation
    form_class = FertilizationRecommendationForm


class FertilizationRecommendationDetailView(DetailView):
    model = FertilizationRecommendation


class FertilizationRecommendationUpdateView(UpdateView):
    model = FertilizationRecommendation
    form_class = FertilizationRecommendationForm


class ActivityListView(ListView):
    model = Activity


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm


class ActivityDetailView(DetailView):
    model = Activity


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm


class AgriculturalProgrammeListView(ListView):
    model = AgriculturalProgramme


class AgriculturalProgrammeCreateView(CreateView):
    model = AgriculturalProgramme
    form_class = AgriculturalProgrammeForm


class AgriculturalProgrammeDetailView(DetailView):
    model = AgriculturalProgramme


class AgriculturalProgrammeUpdateView(UpdateView):
    model = AgriculturalProgramme
    form_class = AgriculturalProgrammeForm


class CropListView(ListView):
    model = Crop


class CropCreateView(CreateView):
    model = Crop
    form_class = CropForm


class CropDetailView(DetailView):
    model = Crop


class CropUpdateView(UpdateView):
    model = Crop
    form_class = CropForm


class FieldCultivationListView(ListView):
    model = FieldCultivation


class FieldCultivationCreateView(CreateView):
    model = FieldCultivation
    form_class = FieldCultivationForm


class FieldCultivationDetailView(DetailView):
    model = FieldCultivation


class FieldCultivationUpdateView(UpdateView):
    model = FieldCultivation
    form_class = FieldCultivationForm


class SampleBaseListView(ListView):
    model = SampleBase


class SampleBaseCreateView(CreateView):
    model = SampleBase
    form_class = SampleBaseForm


class SampleBaseDetailView(DetailView):
    model = SampleBase


class SampleBaseUpdateView(UpdateView):
    model = SampleBase
    form_class = SampleBaseForm


class SoilSampleListView(ListView):
    model = SoilSample


class SoilSampleCreateView(CreateView):
    model = SoilSample
    form_class = SoilSampleForm


class SoilSampleDetailView(DetailView):
    model = SoilSample


class SoilSampleUpdateView(UpdateView):
    model = SoilSample
    form_class = SoilSampleForm


class RecordedStatusListView(ListView):
    model = RecordedStatus


class RecordedStatusCreateView(CreateView):
    model = RecordedStatus
    form_class = RecordedStatusForm


class RecordedStatusDetailView(DetailView):
    model = RecordedStatus


class RecordedStatusUpdateView(UpdateView):
    model = RecordedStatus
    form_class = RecordedStatusForm


class HarvestListView(ListView):
    model = Harvest


class HarvestCreateView(CreateView):
    model = Harvest
    form_class = HarvestForm


class HarvestDetailView(DetailView):
    model = Harvest


class HarvestUpdateView(UpdateView):
    model = Harvest
    form_class = HarvestForm


class AnalysisResultListView(ListView):
    model = AnalysisResult


class AnalysisResultCreateView(CreateView):
    model = AnalysisResult
    form_class = AnalysisResultForm


class AnalysisResultDetailView(DetailView):
    model = AnalysisResult


class AnalysisResultUpdateView(UpdateView):
    model = AnalysisResult
    form_class = AnalysisResultForm


class ProgrammePerformanceListView(ListView):
    model = ProgrammePerformance


class ProgrammePerformanceCreateView(CreateView):
    model = ProgrammePerformance
    form_class = ProgrammePerformanceForm


class ProgrammePerformanceDetailView(DetailView):
    model = ProgrammePerformance


class ProgrammePerformanceUpdateView(UpdateView):
    model = ProgrammePerformance
    form_class = ProgrammePerformanceForm


class FertilizerListView(ListView):
    model = Fertilizer


class FertilizerCreateView(CreateView):
    model = Fertilizer
    form_class = FertilizerForm


class FertilizerDetailView(DetailView):
    model = Fertilizer


class FertilizerUpdateView(UpdateView):
    model = Fertilizer
    form_class = FertilizerForm


class FarmFieldListView(ListView):
    model = FarmField


class FarmFieldCreateView(CreateView):
    model = FarmField
    form_class = FarmFieldForm


class FarmFieldDetailView(DetailView):
    model = FarmField


class FarmFieldUpdateView(UpdateView):
    model = FarmField
    form_class = FarmFieldForm


class GenericStatusListView(ListView):
    model = GenericStatus


class GenericStatusCreateView(CreateView):
    model = GenericStatus
    form_class = GenericStatusForm


class GenericStatusDetailView(DetailView):
    model = GenericStatus


class GenericStatusUpdateView(UpdateView):
    model = GenericStatus
    form_class = GenericStatusForm


class CropGrowthStageListView(ListView):
    model = CropGrowthStage


class CropGrowthStageCreateView(CreateView):
    model = CropGrowthStage
    form_class = CropGrowthStageForm


class CropGrowthStageDetailView(DetailView):
    model = CropGrowthStage


class CropGrowthStageUpdateView(UpdateView):
    model = CropGrowthStage
    form_class = CropGrowthStageForm


class CropSpeciesListView(ListView):
    model = CropSpecies


class CropSpeciesCreateView(CreateView):
    model = CropSpecies
    form_class = CropSpeciesForm


class CropSpeciesDetailView(DetailView):
    model = CropSpecies


class CropSpeciesUpdateView(UpdateView):
    model = CropSpecies
    form_class = CropSpeciesForm


class MeasuredKPIListView(ListView):
    model = MeasuredKPI


class MeasuredKPICreateView(CreateView):
    model = MeasuredKPI
    form_class = MeasuredKPIForm


class MeasuredKPIDetailView(DetailView):
    model = MeasuredKPI


class MeasuredKPIUpdateView(UpdateView):
    model = MeasuredKPI
    form_class = MeasuredKPIForm


class LandUseListView(ListView):
    model = LandUse


class LandUseCreateView(CreateView):
    model = LandUse
    form_class = LandUseForm


class LandUseDetailView(DetailView):
    model = LandUse


class LandUseUpdateView(UpdateView):
    model = LandUse
    form_class = LandUseForm


class ContaminationListView(ListView):
    model = Contamination


class ContaminationCreateView(CreateView):
    model = Contamination
    form_class = ContaminationForm


class ContaminationDetailView(DetailView):
    model = Contamination


class ContaminationUpdateView(UpdateView):
    model = Contamination
    form_class = ContaminationForm

