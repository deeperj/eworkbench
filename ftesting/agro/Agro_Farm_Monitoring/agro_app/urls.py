from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'farm', api.FarmViewSet)
router.register(r'farmcertificate', api.FarmCertificateViewSet)
router.register(r'certificationvalidity', api.CertificationValidityViewSet)
router.register(r'farmfield', api.FarmFieldViewSet)
router.register(r'assessment', api.AssessmentViewSet)
router.register(r'genericstatus', api.GenericStatusViewSet)
router.register(r'recordedstatus', api.RecordedStatusViewSet)
router.register(r'landuse', api.LandUseViewSet)
router.register(r'fertilizationrecommendation', api.FertilizationRecommendationViewSet)
router.register(r'samplebase', api.SampleBaseViewSet)
router.register(r'soilsample', api.SoilSampleViewSet)
router.register(r'analysisresult', api.AnalysisResultViewSet)
router.register(r'fertilizer', api.FertilizerViewSet)
router.register(r'fieldcultivation', api.FieldCultivationViewSet)
router.register(r'crop', api.CropViewSet)
router.register(r'cropgrowthstage', api.CropGrowthStageViewSet)
router.register(r'cropspecies', api.CropSpeciesViewSet)
router.register(r'harvest', api.HarvestViewSet)
router.register(r'activity', api.ActivityViewSet)
router.register(r'weather', api.WeatherViewSet)
router.register(r'contamination', api.ContaminationViewSet)
router.register(r'programmeperformance', api.ProgrammePerformanceViewSet)
router.register(r'measuredkpi', api.MeasuredKPIViewSet)
router.register(r'agrodocument', api.AgroDocumentViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Farm
    path('agro_app/farm/', views.FarmListView.as_view(), name='agro_app_farm_list'),
    path('agro_app/farm/create/', views.FarmCreateView.as_view(), name='agro_app_farm_create'),
    path('agro_app/farm/detail/<int:pk>/', views.FarmDetailView.as_view(), name='agro_app_farm_detail'),
    path('agro_app/farm/update/<int:pk>/', views.FarmUpdateView.as_view(), name='agro_app_farm_update'),
)

urlpatterns += (
    # urls for FarmCertificate
    path('agro_app/farmcertificate/', views.FarmCertificateListView.as_view(), name='agro_app_farmcertificate_list'),
    path('agro_app/farmcertificate/create/', views.FarmCertificateCreateView.as_view(), name='agro_app_farmcertificate_create'),
    path('agro_app/farmcertificate/detail/<int:pk>/', views.FarmCertificateDetailView.as_view(), name='agro_app_farmcertificate_detail'),
    path('agro_app/farmcertificate/update/<int:pk>/', views.FarmCertificateUpdateView.as_view(), name='agro_app_farmcertificate_update'),
)

urlpatterns += (
    # urls for CertificationValidity
    path('agro_app/certificationvalidity/', views.CertificationValidityListView.as_view(), name='agro_app_certificationvalidity_list'),
    path('agro_app/certificationvalidity/create/', views.CertificationValidityCreateView.as_view(), name='agro_app_certificationvalidity_create'),
    path('agro_app/certificationvalidity/detail/<int:pk>/', views.CertificationValidityDetailView.as_view(), name='agro_app_certificationvalidity_detail'),
    path('agro_app/certificationvalidity/update/<int:pk>/', views.CertificationValidityUpdateView.as_view(), name='agro_app_certificationvalidity_update'),
)

urlpatterns += (
    # urls for FarmField
    path('agro_app/farmfield/', views.FarmFieldListView.as_view(), name='agro_app_farmfield_list'),
    path('agro_app/farmfield/create/', views.FarmFieldCreateView.as_view(), name='agro_app_farmfield_create'),
    path('agro_app/farmfield/detail/<int:pk>/', views.FarmFieldDetailView.as_view(), name='agro_app_farmfield_detail'),
    path('agro_app/farmfield/update/<int:pk>/', views.FarmFieldUpdateView.as_view(), name='agro_app_farmfield_update'),
)

urlpatterns += (
    # urls for Assessment
    path('agro_app/assessment/', views.AssessmentListView.as_view(), name='agro_app_assessment_list'),
    path('agro_app/assessment/create/', views.AssessmentCreateView.as_view(), name='agro_app_assessment_create'),
    path('agro_app/assessment/detail/<int:pk>/', views.AssessmentDetailView.as_view(), name='agro_app_assessment_detail'),
    path('agro_app/assessment/update/<int:pk>/', views.AssessmentUpdateView.as_view(), name='agro_app_assessment_update'),
)

urlpatterns += (
    # urls for GenericStatus
    path('agro_app/genericstatus/', views.GenericStatusListView.as_view(), name='agro_app_genericstatus_list'),
    path('agro_app/genericstatus/create/', views.GenericStatusCreateView.as_view(), name='agro_app_genericstatus_create'),
    path('agro_app/genericstatus/detail/<int:pk>/', views.GenericStatusDetailView.as_view(), name='agro_app_genericstatus_detail'),
    path('agro_app/genericstatus/update/<int:pk>/', views.GenericStatusUpdateView.as_view(), name='agro_app_genericstatus_update'),
)

urlpatterns += (
    # urls for RecordedStatus
    path('agro_app/recordedstatus/', views.RecordedStatusListView.as_view(), name='agro_app_recordedstatus_list'),
    path('agro_app/recordedstatus/create/', views.RecordedStatusCreateView.as_view(), name='agro_app_recordedstatus_create'),
    path('agro_app/recordedstatus/detail/<int:pk>/', views.RecordedStatusDetailView.as_view(), name='agro_app_recordedstatus_detail'),
    path('agro_app/recordedstatus/update/<int:pk>/', views.RecordedStatusUpdateView.as_view(), name='agro_app_recordedstatus_update'),
)

urlpatterns += (
    # urls for LandUse
    path('agro_app/landuse/', views.LandUseListView.as_view(), name='agro_app_landuse_list'),
    path('agro_app/landuse/create/', views.LandUseCreateView.as_view(), name='agro_app_landuse_create'),
    path('agro_app/landuse/detail/<int:pk>/', views.LandUseDetailView.as_view(), name='agro_app_landuse_detail'),
    path('agro_app/landuse/update/<int:pk>/', views.LandUseUpdateView.as_view(), name='agro_app_landuse_update'),
)

urlpatterns += (
    # urls for FertilizationRecommendation
    path('agro_app/fertilizationrecommendation/', views.FertilizationRecommendationListView.as_view(), name='agro_app_fertilizationrecommendation_list'),
    path('agro_app/fertilizationrecommendation/create/', views.FertilizationRecommendationCreateView.as_view(), name='agro_app_fertilizationrecommendation_create'),
    path('agro_app/fertilizationrecommendation/detail/<int:pk>/', views.FertilizationRecommendationDetailView.as_view(), name='agro_app_fertilizationrecommendation_detail'),
    path('agro_app/fertilizationrecommendation/update/<int:pk>/', views.FertilizationRecommendationUpdateView.as_view(), name='agro_app_fertilizationrecommendation_update'),
)

urlpatterns += (
    # urls for SampleBase
    path('agro_app/samplebase/', views.SampleBaseListView.as_view(), name='agro_app_samplebase_list'),
    path('agro_app/samplebase/create/', views.SampleBaseCreateView.as_view(), name='agro_app_samplebase_create'),
    path('agro_app/samplebase/detail/<int:pk>/', views.SampleBaseDetailView.as_view(), name='agro_app_samplebase_detail'),
    path('agro_app/samplebase/update/<int:pk>/', views.SampleBaseUpdateView.as_view(), name='agro_app_samplebase_update'),
)

urlpatterns += (
    # urls for SoilSample
    path('agro_app/soilsample/', views.SoilSampleListView.as_view(), name='agro_app_soilsample_list'),
    path('agro_app/soilsample/create/', views.SoilSampleCreateView.as_view(), name='agro_app_soilsample_create'),
    path('agro_app/soilsample/detail/<int:pk>/', views.SoilSampleDetailView.as_view(), name='agro_app_soilsample_detail'),
    path('agro_app/soilsample/update/<int:pk>/', views.SoilSampleUpdateView.as_view(), name='agro_app_soilsample_update'),
)

urlpatterns += (
    # urls for AnalysisResult
    path('agro_app/analysisresult/', views.AnalysisResultListView.as_view(), name='agro_app_analysisresult_list'),
    path('agro_app/analysisresult/create/', views.AnalysisResultCreateView.as_view(), name='agro_app_analysisresult_create'),
    path('agro_app/analysisresult/detail/<int:pk>/', views.AnalysisResultDetailView.as_view(), name='agro_app_analysisresult_detail'),
    path('agro_app/analysisresult/update/<int:pk>/', views.AnalysisResultUpdateView.as_view(), name='agro_app_analysisresult_update'),
)

urlpatterns += (
    # urls for Fertilizer
    path('agro_app/fertilizer/', views.FertilizerListView.as_view(), name='agro_app_fertilizer_list'),
    path('agro_app/fertilizer/create/', views.FertilizerCreateView.as_view(), name='agro_app_fertilizer_create'),
    path('agro_app/fertilizer/detail/<int:pk>/', views.FertilizerDetailView.as_view(), name='agro_app_fertilizer_detail'),
    path('agro_app/fertilizer/update/<int:pk>/', views.FertilizerUpdateView.as_view(), name='agro_app_fertilizer_update'),
)

urlpatterns += (
    # urls for FieldCultivation
    path('agro_app/fieldcultivation/', views.FieldCultivationListView.as_view(), name='agro_app_fieldcultivation_list'),
    path('agro_app/fieldcultivation/create/', views.FieldCultivationCreateView.as_view(), name='agro_app_fieldcultivation_create'),
    path('agro_app/fieldcultivation/detail/<int:pk>/', views.FieldCultivationDetailView.as_view(), name='agro_app_fieldcultivation_detail'),
    path('agro_app/fieldcultivation/update/<int:pk>/', views.FieldCultivationUpdateView.as_view(), name='agro_app_fieldcultivation_update'),
)

urlpatterns += (
    # urls for Crop
    path('agro_app/crop/', views.CropListView.as_view(), name='agro_app_crop_list'),
    path('agro_app/crop/create/', views.CropCreateView.as_view(), name='agro_app_crop_create'),
    path('agro_app/crop/detail/<int:pk>/', views.CropDetailView.as_view(), name='agro_app_crop_detail'),
    path('agro_app/crop/update/<int:pk>/', views.CropUpdateView.as_view(), name='agro_app_crop_update'),
)

urlpatterns += (
    # urls for CropGrowthStage
    path('agro_app/cropgrowthstage/', views.CropGrowthStageListView.as_view(), name='agro_app_cropgrowthstage_list'),
    path('agro_app/cropgrowthstage/create/', views.CropGrowthStageCreateView.as_view(), name='agro_app_cropgrowthstage_create'),
    path('agro_app/cropgrowthstage/detail/<int:pk>/', views.CropGrowthStageDetailView.as_view(), name='agro_app_cropgrowthstage_detail'),
    path('agro_app/cropgrowthstage/update/<int:pk>/', views.CropGrowthStageUpdateView.as_view(), name='agro_app_cropgrowthstage_update'),
)

urlpatterns += (
    # urls for CropSpecies
    path('agro_app/cropspecies/', views.CropSpeciesListView.as_view(), name='agro_app_cropspecies_list'),
    path('agro_app/cropspecies/create/', views.CropSpeciesCreateView.as_view(), name='agro_app_cropspecies_create'),
    path('agro_app/cropspecies/detail/<int:pk>/', views.CropSpeciesDetailView.as_view(), name='agro_app_cropspecies_detail'),
    path('agro_app/cropspecies/update/<int:pk>/', views.CropSpeciesUpdateView.as_view(), name='agro_app_cropspecies_update'),
)

urlpatterns += (
    # urls for Harvest
    path('agro_app/harvest/', views.HarvestListView.as_view(), name='agro_app_harvest_list'),
    path('agro_app/harvest/create/', views.HarvestCreateView.as_view(), name='agro_app_harvest_create'),
    path('agro_app/harvest/detail/<int:pk>/', views.HarvestDetailView.as_view(), name='agro_app_harvest_detail'),
    path('agro_app/harvest/update/<int:pk>/', views.HarvestUpdateView.as_view(), name='agro_app_harvest_update'),
)

urlpatterns += (
    # urls for Activity
    path('agro_app/activity/', views.ActivityListView.as_view(), name='agro_app_activity_list'),
    path('agro_app/activity/create/', views.ActivityCreateView.as_view(), name='agro_app_activity_create'),
    path('agro_app/activity/detail/<int:pk>/', views.ActivityDetailView.as_view(), name='agro_app_activity_detail'),
    path('agro_app/activity/update/<int:pk>/', views.ActivityUpdateView.as_view(), name='agro_app_activity_update'),
)

urlpatterns += (
    # urls for Weather
    path('agro_app/weather/', views.WeatherListView.as_view(), name='agro_app_weather_list'),
    path('agro_app/weather/create/', views.WeatherCreateView.as_view(), name='agro_app_weather_create'),
    path('agro_app/weather/detail/<int:pk>/', views.WeatherDetailView.as_view(), name='agro_app_weather_detail'),
    path('agro_app/weather/update/<int:pk>/', views.WeatherUpdateView.as_view(), name='agro_app_weather_update'),
)

urlpatterns += (
    # urls for Contamination
    path('agro_app/contamination/', views.ContaminationListView.as_view(), name='agro_app_contamination_list'),
    path('agro_app/contamination/create/', views.ContaminationCreateView.as_view(), name='agro_app_contamination_create'),
    path('agro_app/contamination/detail/<int:pk>/', views.ContaminationDetailView.as_view(), name='agro_app_contamination_detail'),
    path('agro_app/contamination/update/<int:pk>/', views.ContaminationUpdateView.as_view(), name='agro_app_contamination_update'),
)

urlpatterns += (
    # urls for ProgrammePerformance
    path('agro_app/programmeperformance/', views.ProgrammePerformanceListView.as_view(), name='agro_app_programmeperformance_list'),
    path('agro_app/programmeperformance/create/', views.ProgrammePerformanceCreateView.as_view(), name='agro_app_programmeperformance_create'),
    path('agro_app/programmeperformance/detail/<int:pk>/', views.ProgrammePerformanceDetailView.as_view(), name='agro_app_programmeperformance_detail'),
    path('agro_app/programmeperformance/update/<int:pk>/', views.ProgrammePerformanceUpdateView.as_view(), name='agro_app_programmeperformance_update'),
)

urlpatterns += (
    # urls for MeasuredKPI
    path('agro_app/measuredkpi/', views.MeasuredKPIListView.as_view(), name='agro_app_measuredkpi_list'),
    path('agro_app/measuredkpi/create/', views.MeasuredKPICreateView.as_view(), name='agro_app_measuredkpi_create'),
    path('agro_app/measuredkpi/detail/<int:pk>/', views.MeasuredKPIDetailView.as_view(), name='agro_app_measuredkpi_detail'),
    path('agro_app/measuredkpi/update/<int:pk>/', views.MeasuredKPIUpdateView.as_view(), name='agro_app_measuredkpi_update'),
)

urlpatterns += (
    # urls for AgroDocument
    path('agro_app/agrodocument/', views.AgroDocumentListView.as_view(), name='agro_app_agrodocument_list'),
    path('agro_app/agrodocument/create/', views.AgroDocumentCreateView.as_view(), name='agro_app_agrodocument_create'),
    path('agro_app/agrodocument/detail/<int:pk>/', views.AgroDocumentDetailView.as_view(), name='agro_app_agrodocument_detail'),
    path('agro_app/agrodocument/update/<int:pk>/', views.AgroDocumentUpdateView.as_view(), name='agro_app_agrodocument_update'),
)

