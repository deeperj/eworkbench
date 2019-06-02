import unittest
from django.urls import reverse
from django.test import Client
from .models import Farm, FarmCertificate, CertificationValidity, FarmField, Assessment, GenericStatus, RecordedStatus, LandUse, FertilizationRecommendation, SampleBase, SoilSample, AnalysisResult, Fertilizer, FieldCultivation, Crop, CropGrowthStage, CropSpecies, Harvest, Activity, Weather, Contamination, ProgrammePerformance, MeasuredKPI, AgroDocument
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_farm(**kwargs):
    defaults = {}
    defaults["description"] = "description"
    defaults["purpose"] = "purpose"
    defaults["farming_system"] = "farming_system"
    defaults.update(**kwargs)
    if "owner" not in defaults:
        defaults["owner"] = create_user()
    return Farm.objects.create(**defaults)


def create_farmcertificate(**kwargs):
    defaults = {}
    defaults["first_certificate_date"] = "first_certificate_date"
    defaults["certification_agency"] = "certification_agency"
    defaults["certificate_number"] = "certificate_number"
    defaults["certification_code"] = "certification_code"
    defaults["supporting_documents"] = "supporting_documents"
    defaults.update(**kwargs)
    return FarmCertificate.objects.create(**defaults)


def create_certificationvalidity(**kwargs):
    defaults = {}
    defaults["valid_for_purpose"] = "valid_for_purpose"
    defaults["farm_purpose"] = "farm_purpose"
    defaults["issue_date"] = "issue_date"
    defaults["expiry_date"] = "expiry_date"
    defaults.update(**kwargs)
    return CertificationValidity.objects.create(**defaults)


def create_farmfield(**kwargs):
    defaults = {}
    defaults["name_of_field"] = "name_of_field"
    defaults["field_identification"] = "field_identification"
    defaults["unique_area_id"] = "unique_area_id"
    defaults["area"] = "area"
    defaults["area_unit"] = "area_unit"
    defaults["spatial_data"] = "spatial_data"
    defaults.update(**kwargs)
    if "cultivation" not in defaults:
        defaults["cultivation"] = create_cultivation()
    if "land_use_restriction" not in defaults:
        defaults["land_use_restriction"] = create_'landuse'()
    if "assessment" not in defaults:
        defaults["assessment"] = create_'assessment'()
    return FarmField.objects.create(**defaults)


def create_assessment(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "analysis" not in defaults:
        defaults["analysis"] = create_'analysis'()
    if "status" not in defaults:
        defaults["status"] = create_'recordedstatus'()
    return Assessment.objects.create(**defaults)


def create_genericstatus(**kwargs):
    defaults = {}
    defaults["staus"] = "staus"
    defaults["status_name"] = "status_name"
    defaults["meaning"] = "meaning"
    defaults.update(**kwargs)
    return GenericStatus.objects.create(**defaults)


def create_recordedstatus(**kwargs):
    defaults = {}
    defaults["status_date"] = "status_date"
    defaults["status_time"] = "status_time"
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_'genericstatus'()
    return RecordedStatus.objects.create(**defaults)


def create_landuse(**kwargs):
    defaults = {}
    defaults["land_use_restriction_type"] = "land_use_restriction_type"
    defaults.update(**kwargs)
    return LandUse.objects.create(**defaults)


def create_fertilizationrecommendation(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return FertilizationRecommendation.objects.create(**defaults)


def create_samplebase(**kwargs):
    defaults = {}
    defaults["recieved_date"] = "recieved_date"
    defaults["received_time"] = "received_time"
    defaults["description"] = "description"
    defaults["comment"] = "comment"
    defaults["weight"] = "weight"
    defaults["weight_unit"] = "weight_unit"
    defaults["volume"] = "volume"
    defaults["volume_unit"] = "volume_unit"
    defaults["analysis_date"] = "analysis_date"
    defaults["analysis_time"] = "analysis_time"
    defaults.update(**kwargs)
    return SampleBase.objects.create(**defaults)


def create_soilsample(**kwargs):
    defaults = {}
    defaults["soil_name"] = "soil_name"
    defaults["soil_type"] = "soil_type"
    defaults["reference_part_of_field"] = "reference_part_of_field"
    defaults["spatial_data"] = "spatial_data"
    defaults["depth"] = "depth"
    defaults["depth_unit"] = "depth_unit"
    defaults["depth_range"] = "depth_range"
    defaults["analysis_method"] = "analysis_method"
    defaults["soil_heaviness"] = "soil_heaviness"
    defaults["soil_nutrient_classification"] = "soil_nutrient_classification"
    defaults["soil_texture"] = "soil_texture"
    defaults.update(**kwargs)
    return SoilSample.objects.create(**defaults)


def create_analysisresult(**kwargs):
    defaults = {}
    defaults["abstract_analysis"] = "abstract_analysis"
    defaults["description"] = "description"
    defaults["method"] = "method"
    defaults["comment"] = "comment"
    defaults.update(**kwargs)
    if "sample" not in defaults:
        defaults["sample"] = create_'reportedsample'()
    return AnalysisResult.objects.create(**defaults)


def create_fertilizer(**kwargs):
    defaults = {}
    defaults["fertilizer_brand"] = "fertilizer_brand"
    defaults["fertlizer_name"] = "fertlizer_name"
    defaults["fertilizer_type"] = "fertilizer_type"
    defaults["fertilizer_form"] = "fertilizer_form"
    defaults.update(**kwargs)
    return Fertilizer.objects.create(**defaults)


def create_fieldcultivation(**kwargs):
    defaults = {}
    defaults["duration_of_use"] = "duration_of_use"
    defaults["duration_unit"] = "duration_unit"
    defaults.update(**kwargs)
    if "farm_field" not in defaults:
        defaults["farm_field"] = create_'farmfield'()
    if "reference_field_part" not in defaults:
        defaults["reference_field_part"] = create_'farmfield'()
    return FieldCultivation.objects.create(**defaults)


def create_crop(**kwargs):
    defaults = {}
    defaults["monetary_value_per_hectar"] = "monetary_value_per_hectar"
    defaults["monetary_value_currency"] = "monetary_value_currency"
    defaults["botanical_name"] = "botanical_name"
    defaults.update(**kwargs)
    if "farm_field" not in defaults:
        defaults["farm_field"] = create_'farmfield'()
    if "crop_growth_event" not in defaults:
        defaults["crop_growth_event"] = create_'cropgrowthstage'()
    return Crop.objects.create(**defaults)


def create_cropgrowthstage(**kwargs):
    defaults = {}
    defaults["growth_stage"] = "growth_stage"
    defaults["date_recorded"] = "date_recorded"
    defaults["time_recorded"] = "time_recorded"
    defaults.update(**kwargs)
    return CropGrowthStage.objects.create(**defaults)


def create_cropspecies(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["variety"] = "variety"
    defaults["genetically_modified_organism"] = "genetically_modified_organism"
    defaults.update(**kwargs)
    if "crop" not in defaults:
        defaults["crop"] = create_'crop'()
    return CropSpecies.objects.create(**defaults)


def create_harvest(**kwargs):
    defaults = {}
    defaults["harvested_quantity"] = "harvested_quantity"
    defaults["yield_quantity"] = "yield_quantity"
    defaults["quantity_unit"] = "quantity_unit"
    defaults["harvest_quality"] = "harvest_quality"
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults.update(**kwargs)
    if "crop" not in defaults:
        defaults["crop"] = create_'crop'()
    if "farm_field" not in defaults:
        defaults["farm_field"] = create_'farmfield'()
    return Harvest.objects.create(**defaults)


def create_activity(**kwargs):
    defaults = {}
    defaults["daily_start"] = "daily_start"
    defaults["daily_end"] = "daily_end"
    defaults["activity"] = "activity"
    defaults["comment"] = "comment"
    defaults["work_done"] = "work_done"
    defaults["percentage_executed"] = "percentage_executed"
    defaults.update(**kwargs)
    return Activity.objects.create(**defaults)


def create_weather(**kwargs):
    defaults = {}
    defaults["temperature"] = "temperature"
    defaults["temperature_unit"] = "temperature_unit"
    defaults["wind_speed"] = "wind_speed"
    defaults["wind_speed_unit"] = "wind_speed_unit"
    defaults["humidity"] = "humidity"
    defaults["humidity_unit"] = "humidity_unit"
    defaults["precipitation"] = "precipitation"
    defaults["precipitation_unit"] = "precipitation_unit"
    defaults["solar_radiation"] = "solar_radiation"
    defaults["solar_radiation_unit"] = "solar_radiation_unit"
    defaults["reported_date"] = "reported_date"
    defaults["reported_time"] = "reported_time"
    defaults["measured_date"] = "measured_date"
    defaults["measured_time"] = "measured_time"
    defaults.update(**kwargs)
    if "reported_by" not in defaults:
        defaults["reported_by"] = create_'user'()
    if "measured_by" not in defaults:
        defaults["measured_by"] = create_'user'()
    return Weather.objects.create(**defaults)


def create_contamination(**kwargs):
    defaults = {}
    defaults["contaimination_type"] = "contaimination_type"
    defaults["contamination_degree"] = "contamination_degree"
    defaults["noticed_date"] = "noticed_date"
    defaults["noticed_time"] = "noticed_time"
    defaults["start"] = "start"
    defaults["end"] = "end"
    defaults["invitations"] = "invitations"
    defaults["consultants"] = "consultants"
    defaults["purpose"] = "purpose"
    defaults["description"] = "description"
    defaults["targets"] = "targets"
    defaults["comments"] = "comments"
    defaults.update(**kwargs)
    if "reported_by" not in defaults:
        defaults["reported_by"] = create_'user'()
    if "affected_fields" not in defaults:
        defaults["affected_fields"] = create_'farmfield'()
    if "kpis" not in defaults:
        defaults["kpis"] = create_'measuredkpi'()
    if "status" not in defaults:
        defaults["status"] = create_'recordedstatus'()
    return Contamination.objects.create(**defaults)


def create_programmeperformance(**kwargs):
    defaults = {}
    defaults["comments"] = "comments"
    defaults["learning_points"] = "learning_points"
    defaults["recommendations"] = "recommendations"
    defaults["participant_suggestions"] = "participant_suggestions"
    defaults.update(**kwargs)
    return ProgrammePerformance.objects.create(**defaults)


def create_measuredkpi(**kwargs):
    defaults = {}
    defaults["measured_kpis"] = "measured_kpis"
    defaults["impact_assessment"] = "impact_assessment"
    defaults.update(**kwargs)
    if "programme_performance" not in defaults:
        defaults["programme_performance"] = create_'programmeperformance'()
    if "fertilizer" not in defaults:
        defaults["fertilizer"] = create_'fertilizer'()
    return MeasuredKPI.objects.create(**defaults)


def create_agrodocument(**kwargs):
    defaults = {}
    defaults["profile"] = "profile"
    defaults.update(**kwargs)
    if "farm" not in defaults:
        defaults["farm"] = create_farm()
    if "work_process" not in defaults:
        defaults["work_process"] = create_wokprocess()
    return AgroDocument.objects.create(**defaults)


class FarmViewTest(unittest.TestCase):
    '''
    Tests for Farm
    '''
    def setUp(self):
        self.client = Client()

    def test_list_farm(self):
        url = reverse('agro_app_farm_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_farm(self):
        url = reverse('agro_app_farm_create')
        data = {
            "description": "description",
            "purpose": "purpose",
            "farming_system": "farming_system",
            "owner": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_farm(self):
        farm = create_farm()
        url = reverse('agro_app_farm_detail', args=[farm.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_farm(self):
        farm = create_farm()
        data = {
            "description": "description",
            "purpose": "purpose",
            "farming_system": "farming_system",
            "owner": create_user().pk,
        }
        url = reverse('agro_app_farm_update', args=[farm.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FarmCertificateViewTest(unittest.TestCase):
    '''
    Tests for FarmCertificate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_farmcertificate(self):
        url = reverse('agro_app_farmcertificate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_farmcertificate(self):
        url = reverse('agro_app_farmcertificate_create')
        data = {
            "first_certificate_date": "first_certificate_date",
            "certification_agency": "certification_agency",
            "certificate_number": "certificate_number",
            "certification_code": "certification_code",
            "supporting_documents": "supporting_documents",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_farmcertificate(self):
        farmcertificate = create_farmcertificate()
        url = reverse('agro_app_farmcertificate_detail', args=[farmcertificate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_farmcertificate(self):
        farmcertificate = create_farmcertificate()
        data = {
            "first_certificate_date": "first_certificate_date",
            "certification_agency": "certification_agency",
            "certificate_number": "certificate_number",
            "certification_code": "certification_code",
            "supporting_documents": "supporting_documents",
        }
        url = reverse('agro_app_farmcertificate_update', args=[farmcertificate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CertificationValidityViewTest(unittest.TestCase):
    '''
    Tests for CertificationValidity
    '''
    def setUp(self):
        self.client = Client()

    def test_list_certificationvalidity(self):
        url = reverse('agro_app_certificationvalidity_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_certificationvalidity(self):
        url = reverse('agro_app_certificationvalidity_create')
        data = {
            "valid_for_purpose": "valid_for_purpose",
            "farm_purpose": "farm_purpose",
            "issue_date": "issue_date",
            "expiry_date": "expiry_date",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_certificationvalidity(self):
        certificationvalidity = create_certificationvalidity()
        url = reverse('agro_app_certificationvalidity_detail', args=[certificationvalidity.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_certificationvalidity(self):
        certificationvalidity = create_certificationvalidity()
        data = {
            "valid_for_purpose": "valid_for_purpose",
            "farm_purpose": "farm_purpose",
            "issue_date": "issue_date",
            "expiry_date": "expiry_date",
        }
        url = reverse('agro_app_certificationvalidity_update', args=[certificationvalidity.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FarmFieldViewTest(unittest.TestCase):
    '''
    Tests for FarmField
    '''
    def setUp(self):
        self.client = Client()

    def test_list_farmfield(self):
        url = reverse('agro_app_farmfield_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_farmfield(self):
        url = reverse('agro_app_farmfield_create')
        data = {
            "name_of_field": "name_of_field",
            "field_identification": "field_identification",
            "unique_area_id": "unique_area_id",
            "area": "area",
            "area_unit": "area_unit",
            "spatial_data": "spatial_data",
            "cultivation": create_cultivation().pk,
            "land_use_restriction": create_'landuse'().pk,
            "assessment": create_'assessment'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_farmfield(self):
        farmfield = create_farmfield()
        url = reverse('agro_app_farmfield_detail', args=[farmfield.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_farmfield(self):
        farmfield = create_farmfield()
        data = {
            "name_of_field": "name_of_field",
            "field_identification": "field_identification",
            "unique_area_id": "unique_area_id",
            "area": "area",
            "area_unit": "area_unit",
            "spatial_data": "spatial_data",
            "cultivation": create_cultivation().pk,
            "land_use_restriction": create_'landuse'().pk,
            "assessment": create_'assessment'().pk,
        }
        url = reverse('agro_app_farmfield_update', args=[farmfield.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AssessmentViewTest(unittest.TestCase):
    '''
    Tests for Assessment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_assessment(self):
        url = reverse('agro_app_assessment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_assessment(self):
        url = reverse('agro_app_assessment_create')
        data = {
            "analysis": create_'analysis'().pk,
            "status": create_'recordedstatus'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_assessment(self):
        assessment = create_assessment()
        url = reverse('agro_app_assessment_detail', args=[assessment.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_assessment(self):
        assessment = create_assessment()
        data = {
            "analysis": create_'analysis'().pk,
            "status": create_'recordedstatus'().pk,
        }
        url = reverse('agro_app_assessment_update', args=[assessment.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GenericStatusViewTest(unittest.TestCase):
    '''
    Tests for GenericStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_genericstatus(self):
        url = reverse('agro_app_genericstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_genericstatus(self):
        url = reverse('agro_app_genericstatus_create')
        data = {
            "staus": "staus",
            "status_name": "status_name",
            "meaning": "meaning",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_genericstatus(self):
        genericstatus = create_genericstatus()
        url = reverse('agro_app_genericstatus_detail', args=[genericstatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_genericstatus(self):
        genericstatus = create_genericstatus()
        data = {
            "staus": "staus",
            "status_name": "status_name",
            "meaning": "meaning",
        }
        url = reverse('agro_app_genericstatus_update', args=[genericstatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RecordedStatusViewTest(unittest.TestCase):
    '''
    Tests for RecordedStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_recordedstatus(self):
        url = reverse('agro_app_recordedstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_recordedstatus(self):
        url = reverse('agro_app_recordedstatus_create')
        data = {
            "status_date": "status_date",
            "status_time": "status_time",
            "status": create_'genericstatus'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_recordedstatus(self):
        recordedstatus = create_recordedstatus()
        url = reverse('agro_app_recordedstatus_detail', args=[recordedstatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_recordedstatus(self):
        recordedstatus = create_recordedstatus()
        data = {
            "status_date": "status_date",
            "status_time": "status_time",
            "status": create_'genericstatus'().pk,
        }
        url = reverse('agro_app_recordedstatus_update', args=[recordedstatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LandUseViewTest(unittest.TestCase):
    '''
    Tests for LandUse
    '''
    def setUp(self):
        self.client = Client()

    def test_list_landuse(self):
        url = reverse('agro_app_landuse_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_landuse(self):
        url = reverse('agro_app_landuse_create')
        data = {
            "land_use_restriction_type": "land_use_restriction_type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_landuse(self):
        landuse = create_landuse()
        url = reverse('agro_app_landuse_detail', args=[landuse.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_landuse(self):
        landuse = create_landuse()
        data = {
            "land_use_restriction_type": "land_use_restriction_type",
        }
        url = reverse('agro_app_landuse_update', args=[landuse.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FertilizationRecommendationViewTest(unittest.TestCase):
    '''
    Tests for FertilizationRecommendation
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fertilizationrecommendation(self):
        url = reverse('agro_app_fertilizationrecommendation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fertilizationrecommendation(self):
        url = reverse('agro_app_fertilizationrecommendation_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fertilizationrecommendation(self):
        fertilizationrecommendation = create_fertilizationrecommendation()
        url = reverse('agro_app_fertilizationrecommendation_detail', args=[fertilizationrecommendation.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fertilizationrecommendation(self):
        fertilizationrecommendation = create_fertilizationrecommendation()
        data = {
        }
        url = reverse('agro_app_fertilizationrecommendation_update', args=[fertilizationrecommendation.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SampleBaseViewTest(unittest.TestCase):
    '''
    Tests for SampleBase
    '''
    def setUp(self):
        self.client = Client()

    def test_list_samplebase(self):
        url = reverse('agro_app_samplebase_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_samplebase(self):
        url = reverse('agro_app_samplebase_create')
        data = {
            "recieved_date": "recieved_date",
            "received_time": "received_time",
            "description": "description",
            "comment": "comment",
            "weight": "weight",
            "weight_unit": "weight_unit",
            "volume": "volume",
            "volume_unit": "volume_unit",
            "analysis_date": "analysis_date",
            "analysis_time": "analysis_time",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_samplebase(self):
        samplebase = create_samplebase()
        url = reverse('agro_app_samplebase_detail', args=[samplebase.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_samplebase(self):
        samplebase = create_samplebase()
        data = {
            "recieved_date": "recieved_date",
            "received_time": "received_time",
            "description": "description",
            "comment": "comment",
            "weight": "weight",
            "weight_unit": "weight_unit",
            "volume": "volume",
            "volume_unit": "volume_unit",
            "analysis_date": "analysis_date",
            "analysis_time": "analysis_time",
        }
        url = reverse('agro_app_samplebase_update', args=[samplebase.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SoilSampleViewTest(unittest.TestCase):
    '''
    Tests for SoilSample
    '''
    def setUp(self):
        self.client = Client()

    def test_list_soilsample(self):
        url = reverse('agro_app_soilsample_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_soilsample(self):
        url = reverse('agro_app_soilsample_create')
        data = {
            "soil_name": "soil_name",
            "soil_type": "soil_type",
            "reference_part_of_field": "reference_part_of_field",
            "spatial_data": "spatial_data",
            "depth": "depth",
            "depth_unit": "depth_unit",
            "depth_range": "depth_range",
            "analysis_method": "analysis_method",
            "soil_heaviness": "soil_heaviness",
            "soil_nutrient_classification": "soil_nutrient_classification",
            "soil_texture": "soil_texture",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_soilsample(self):
        soilsample = create_soilsample()
        url = reverse('agro_app_soilsample_detail', args=[soilsample.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_soilsample(self):
        soilsample = create_soilsample()
        data = {
            "soil_name": "soil_name",
            "soil_type": "soil_type",
            "reference_part_of_field": "reference_part_of_field",
            "spatial_data": "spatial_data",
            "depth": "depth",
            "depth_unit": "depth_unit",
            "depth_range": "depth_range",
            "analysis_method": "analysis_method",
            "soil_heaviness": "soil_heaviness",
            "soil_nutrient_classification": "soil_nutrient_classification",
            "soil_texture": "soil_texture",
        }
        url = reverse('agro_app_soilsample_update', args=[soilsample.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AnalysisResultViewTest(unittest.TestCase):
    '''
    Tests for AnalysisResult
    '''
    def setUp(self):
        self.client = Client()

    def test_list_analysisresult(self):
        url = reverse('agro_app_analysisresult_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_analysisresult(self):
        url = reverse('agro_app_analysisresult_create')
        data = {
            "abstract_analysis": "abstract_analysis",
            "description": "description",
            "method": "method",
            "comment": "comment",
            "sample": create_'reportedsample'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_analysisresult(self):
        analysisresult = create_analysisresult()
        url = reverse('agro_app_analysisresult_detail', args=[analysisresult.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_analysisresult(self):
        analysisresult = create_analysisresult()
        data = {
            "abstract_analysis": "abstract_analysis",
            "description": "description",
            "method": "method",
            "comment": "comment",
            "sample": create_'reportedsample'().pk,
        }
        url = reverse('agro_app_analysisresult_update', args=[analysisresult.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FertilizerViewTest(unittest.TestCase):
    '''
    Tests for Fertilizer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fertilizer(self):
        url = reverse('agro_app_fertilizer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fertilizer(self):
        url = reverse('agro_app_fertilizer_create')
        data = {
            "fertilizer_brand": "fertilizer_brand",
            "fertlizer_name": "fertlizer_name",
            "fertilizer_type": "fertilizer_type",
            "fertilizer_form": "fertilizer_form",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fertilizer(self):
        fertilizer = create_fertilizer()
        url = reverse('agro_app_fertilizer_detail', args=[fertilizer.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fertilizer(self):
        fertilizer = create_fertilizer()
        data = {
            "fertilizer_brand": "fertilizer_brand",
            "fertlizer_name": "fertlizer_name",
            "fertilizer_type": "fertilizer_type",
            "fertilizer_form": "fertilizer_form",
        }
        url = reverse('agro_app_fertilizer_update', args=[fertilizer.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FieldCultivationViewTest(unittest.TestCase):
    '''
    Tests for FieldCultivation
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fieldcultivation(self):
        url = reverse('agro_app_fieldcultivation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fieldcultivation(self):
        url = reverse('agro_app_fieldcultivation_create')
        data = {
            "duration_of_use": "duration_of_use",
            "duration_unit": "duration_unit",
            "farm_field": create_'farmfield'().pk,
            "reference_field_part": create_'farmfield'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fieldcultivation(self):
        fieldcultivation = create_fieldcultivation()
        url = reverse('agro_app_fieldcultivation_detail', args=[fieldcultivation.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fieldcultivation(self):
        fieldcultivation = create_fieldcultivation()
        data = {
            "duration_of_use": "duration_of_use",
            "duration_unit": "duration_unit",
            "farm_field": create_'farmfield'().pk,
            "reference_field_part": create_'farmfield'().pk,
        }
        url = reverse('agro_app_fieldcultivation_update', args=[fieldcultivation.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CropViewTest(unittest.TestCase):
    '''
    Tests for Crop
    '''
    def setUp(self):
        self.client = Client()

    def test_list_crop(self):
        url = reverse('agro_app_crop_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_crop(self):
        url = reverse('agro_app_crop_create')
        data = {
            "monetary_value_per_hectar": "monetary_value_per_hectar",
            "monetary_value_currency": "monetary_value_currency",
            "botanical_name": "botanical_name",
            "farm_field": create_'farmfield'().pk,
            "crop_growth_event": create_'cropgrowthstage'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_crop(self):
        crop = create_crop()
        url = reverse('agro_app_crop_detail', args=[crop.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_crop(self):
        crop = create_crop()
        data = {
            "monetary_value_per_hectar": "monetary_value_per_hectar",
            "monetary_value_currency": "monetary_value_currency",
            "botanical_name": "botanical_name",
            "farm_field": create_'farmfield'().pk,
            "crop_growth_event": create_'cropgrowthstage'().pk,
        }
        url = reverse('agro_app_crop_update', args=[crop.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CropGrowthStageViewTest(unittest.TestCase):
    '''
    Tests for CropGrowthStage
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cropgrowthstage(self):
        url = reverse('agro_app_cropgrowthstage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cropgrowthstage(self):
        url = reverse('agro_app_cropgrowthstage_create')
        data = {
            "growth_stage": "growth_stage",
            "date_recorded": "date_recorded",
            "time_recorded": "time_recorded",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cropgrowthstage(self):
        cropgrowthstage = create_cropgrowthstage()
        url = reverse('agro_app_cropgrowthstage_detail', args=[cropgrowthstage.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cropgrowthstage(self):
        cropgrowthstage = create_cropgrowthstage()
        data = {
            "growth_stage": "growth_stage",
            "date_recorded": "date_recorded",
            "time_recorded": "time_recorded",
        }
        url = reverse('agro_app_cropgrowthstage_update', args=[cropgrowthstage.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CropSpeciesViewTest(unittest.TestCase):
    '''
    Tests for CropSpecies
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cropspecies(self):
        url = reverse('agro_app_cropspecies_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cropspecies(self):
        url = reverse('agro_app_cropspecies_create')
        data = {
            "name": "name",
            "variety": "variety",
            "genetically_modified_organism": "genetically_modified_organism",
            "crop": create_'crop'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cropspecies(self):
        cropspecies = create_cropspecies()
        url = reverse('agro_app_cropspecies_detail', args=[cropspecies.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cropspecies(self):
        cropspecies = create_cropspecies()
        data = {
            "name": "name",
            "variety": "variety",
            "genetically_modified_organism": "genetically_modified_organism",
            "crop": create_'crop'().pk,
        }
        url = reverse('agro_app_cropspecies_update', args=[cropspecies.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class HarvestViewTest(unittest.TestCase):
    '''
    Tests for Harvest
    '''
    def setUp(self):
        self.client = Client()

    def test_list_harvest(self):
        url = reverse('agro_app_harvest_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_harvest(self):
        url = reverse('agro_app_harvest_create')
        data = {
            "harvested_quantity": "harvested_quantity",
            "yield_quantity": "yield_quantity",
            "quantity_unit": "quantity_unit",
            "harvest_quality": "harvest_quality",
            "start_date": "start_date",
            "end_date": "end_date",
            "crop": create_'crop'().pk,
            "farm_field": create_'farmfield'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_harvest(self):
        harvest = create_harvest()
        url = reverse('agro_app_harvest_detail', args=[harvest.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_harvest(self):
        harvest = create_harvest()
        data = {
            "harvested_quantity": "harvested_quantity",
            "yield_quantity": "yield_quantity",
            "quantity_unit": "quantity_unit",
            "harvest_quality": "harvest_quality",
            "start_date": "start_date",
            "end_date": "end_date",
            "crop": create_'crop'().pk,
            "farm_field": create_'farmfield'().pk,
        }
        url = reverse('agro_app_harvest_update', args=[harvest.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ActivityViewTest(unittest.TestCase):
    '''
    Tests for Activity
    '''
    def setUp(self):
        self.client = Client()

    def test_list_activity(self):
        url = reverse('agro_app_activity_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_activity(self):
        url = reverse('agro_app_activity_create')
        data = {
            "daily_start": "daily_start",
            "daily_end": "daily_end",
            "activity": "activity",
            "comment": "comment",
            "work_done": "work_done",
            "percentage_executed": "percentage_executed",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_activity(self):
        activity = create_activity()
        url = reverse('agro_app_activity_detail', args=[activity.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_activity(self):
        activity = create_activity()
        data = {
            "daily_start": "daily_start",
            "daily_end": "daily_end",
            "activity": "activity",
            "comment": "comment",
            "work_done": "work_done",
            "percentage_executed": "percentage_executed",
        }
        url = reverse('agro_app_activity_update', args=[activity.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class WeatherViewTest(unittest.TestCase):
    '''
    Tests for Weather
    '''
    def setUp(self):
        self.client = Client()

    def test_list_weather(self):
        url = reverse('agro_app_weather_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_weather(self):
        url = reverse('agro_app_weather_create')
        data = {
            "temperature": "temperature",
            "temperature_unit": "temperature_unit",
            "wind_speed": "wind_speed",
            "wind_speed_unit": "wind_speed_unit",
            "humidity": "humidity",
            "humidity_unit": "humidity_unit",
            "precipitation": "precipitation",
            "precipitation_unit": "precipitation_unit",
            "solar_radiation": "solar_radiation",
            "solar_radiation_unit": "solar_radiation_unit",
            "reported_date": "reported_date",
            "reported_time": "reported_time",
            "measured_date": "measured_date",
            "measured_time": "measured_time",
            "reported_by": create_'user'().pk,
            "measured_by": create_'user'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_weather(self):
        weather = create_weather()
        url = reverse('agro_app_weather_detail', args=[weather.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_weather(self):
        weather = create_weather()
        data = {
            "temperature": "temperature",
            "temperature_unit": "temperature_unit",
            "wind_speed": "wind_speed",
            "wind_speed_unit": "wind_speed_unit",
            "humidity": "humidity",
            "humidity_unit": "humidity_unit",
            "precipitation": "precipitation",
            "precipitation_unit": "precipitation_unit",
            "solar_radiation": "solar_radiation",
            "solar_radiation_unit": "solar_radiation_unit",
            "reported_date": "reported_date",
            "reported_time": "reported_time",
            "measured_date": "measured_date",
            "measured_time": "measured_time",
            "reported_by": create_'user'().pk,
            "measured_by": create_'user'().pk,
        }
        url = reverse('agro_app_weather_update', args=[weather.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ContaminationViewTest(unittest.TestCase):
    '''
    Tests for Contamination
    '''
    def setUp(self):
        self.client = Client()

    def test_list_contamination(self):
        url = reverse('agro_app_contamination_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_contamination(self):
        url = reverse('agro_app_contamination_create')
        data = {
            "contaimination_type": "contaimination_type",
            "contamination_degree": "contamination_degree",
            "noticed_date": "noticed_date",
            "noticed_time": "noticed_time",
            "start": "start",
            "end": "end",
            "invitations": "invitations",
            "consultants": "consultants",
            "purpose": "purpose",
            "description": "description",
            "targets": "targets",
            "comments": "comments",
            "reported_by": create_'user'().pk,
            "affected_fields": create_'farmfield'().pk,
            "kpis": create_'measuredkpi'().pk,
            "status": create_'recordedstatus'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_contamination(self):
        contamination = create_contamination()
        url = reverse('agro_app_contamination_detail', args=[contamination.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_contamination(self):
        contamination = create_contamination()
        data = {
            "contaimination_type": "contaimination_type",
            "contamination_degree": "contamination_degree",
            "noticed_date": "noticed_date",
            "noticed_time": "noticed_time",
            "start": "start",
            "end": "end",
            "invitations": "invitations",
            "consultants": "consultants",
            "purpose": "purpose",
            "description": "description",
            "targets": "targets",
            "comments": "comments",
            "reported_by": create_'user'().pk,
            "affected_fields": create_'farmfield'().pk,
            "kpis": create_'measuredkpi'().pk,
            "status": create_'recordedstatus'().pk,
        }
        url = reverse('agro_app_contamination_update', args=[contamination.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProgrammePerformanceViewTest(unittest.TestCase):
    '''
    Tests for ProgrammePerformance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_programmeperformance(self):
        url = reverse('agro_app_programmeperformance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_programmeperformance(self):
        url = reverse('agro_app_programmeperformance_create')
        data = {
            "comments": "comments",
            "learning_points": "learning_points",
            "recommendations": "recommendations",
            "participant_suggestions": "participant_suggestions",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_programmeperformance(self):
        programmeperformance = create_programmeperformance()
        url = reverse('agro_app_programmeperformance_detail', args=[programmeperformance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_programmeperformance(self):
        programmeperformance = create_programmeperformance()
        data = {
            "comments": "comments",
            "learning_points": "learning_points",
            "recommendations": "recommendations",
            "participant_suggestions": "participant_suggestions",
        }
        url = reverse('agro_app_programmeperformance_update', args=[programmeperformance.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MeasuredKPIViewTest(unittest.TestCase):
    '''
    Tests for MeasuredKPI
    '''
    def setUp(self):
        self.client = Client()

    def test_list_measuredkpi(self):
        url = reverse('agro_app_measuredkpi_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_measuredkpi(self):
        url = reverse('agro_app_measuredkpi_create')
        data = {
            "measured_kpis": "measured_kpis",
            "impact_assessment": "impact_assessment",
            "programme_performance": create_'programmeperformance'().pk,
            "fertilizer": create_'fertilizer'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_measuredkpi(self):
        measuredkpi = create_measuredkpi()
        url = reverse('agro_app_measuredkpi_detail', args=[measuredkpi.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_measuredkpi(self):
        measuredkpi = create_measuredkpi()
        data = {
            "measured_kpis": "measured_kpis",
            "impact_assessment": "impact_assessment",
            "programme_performance": create_'programmeperformance'().pk,
            "fertilizer": create_'fertilizer'().pk,
        }
        url = reverse('agro_app_measuredkpi_update', args=[measuredkpi.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AgroDocumentViewTest(unittest.TestCase):
    '''
    Tests for AgroDocument
    '''
    def setUp(self):
        self.client = Client()

    def test_list_agrodocument(self):
        url = reverse('agro_app_agrodocument_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_agrodocument(self):
        url = reverse('agro_app_agrodocument_create')
        data = {
            "profile": "profile",
            "farm": create_farm().pk,
            "work_process": create_wokprocess().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_agrodocument(self):
        agrodocument = create_agrodocument()
        url = reverse('agro_app_agrodocument_detail', args=[agrodocument.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_agrodocument(self):
        agrodocument = create_agrodocument()
        data = {
            "profile": "profile",
            "farm": create_farm().pk,
            "work_process": create_wokprocess().pk,
        }
        url = reverse('agro_app_agrodocument_update', args=[agrodocument.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


