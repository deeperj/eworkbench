import unittest
from django.urls import reverse
from django.test import Client
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate, FertilizationRecommendation, Activity, AgriculturalProgramme, Crop, FieldCultivation, SampleBase, SoilSample, RecordedStatus, Harvest, AnalysisResult, ProgrammePerformance, Fertilizer, FarmField, GenericStatus, CropGrowthStage, CropSpecies, MeasuredKPI, LandUse, Contamination
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


def create_certificationvalidity(**kwargs):
    defaults = {}
    defaults["valid_for_purpose"] = "valid_for_purpose"
    defaults["farm_purpose"] = "farm_purpose"
    defaults["issue_date"] = "issue_date"
    defaults["start_date"] = "start_date"
    defaults["expiry_date"] = "expiry_date"
    defaults.update(**kwargs)
    return CertificationValidity.objects.create(**defaults)


def create_programperformance(**kwargs):
    defaults = {}
    defaults["participants"] = "participants"
    defaults["program_activities"] = "program_activities"
    defaults["comments"] = "comments"
    defaults["learning_points"] = "learning_points"
    defaults["recommendations"] = "recommendations"
    defaults["participants_suggestions"] = "participants_suggestions"
    defaults["event_coverage"] = "event_coverage"
    defaults.update(**kwargs)
    return ProgramPerformance.objects.create(**defaults)


def create_weather(**kwargs):
    defaults = {}
    defaults["temperature"] = "temperature"
    defaults["temperature_unit"] = "temperature_unit"
    defaults["wind_speed"] = "wind_speed"
    defaults["wind_speed_unit"] = "wind_speed_unit"
    defaults["humidity"] = "humidity"
    defaults.update(**kwargs)
    return Weather.objects.create(**defaults)


def create_agrodocument(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return AgroDocument.objects.create(**defaults)


def create_farm(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Farm.objects.create(**defaults)


def create_certificate(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Certificate.objects.create(**defaults)


def create_fertilizationrecommendation(**kwargs):
    defaults = {}
    defaults["application_measured_unit"] = "application_measured_unit"
    defaults["application_quantity"] = "application_quantity"
    defaults["substance_contained"] = "substance_contained"
    defaults.update(**kwargs)
    return FertilizationRecommendation.objects.create(**defaults)


def create_activity(**kwargs):
    defaults = {}
    defaults["daily_start"] = "daily_start"
    defaults["activity"] = "activity"
    defaults["comment"] = "comment"
    defaults["percentage_executed"] = "percentage_executed"
    defaults["daily_end"] = "daily_end"
    defaults["work_done"] = "work_done"
    defaults.update(**kwargs)
    return Activity.objects.create(**defaults)


def create_agriculturalprogramme(**kwargs):
    defaults = {}
    defaults["comments"] = "comments"
    defaults["end"] = "end"
    defaults["targets"] = "targets"
    defaults["description"] = "description"
    defaults["start"] = "start"
    defaults["purpose"] = "purpose"
    defaults.update(**kwargs)
    return AgriculturalProgramme.objects.create(**defaults)


def create_crop(**kwargs):
    defaults = {}
    defaults["cultural_name"] = "cultural_name"
    defaults["monetary_value_per_hectar"] = "monetary_value_per_hectar"
    defaults["description"] = "description"
    defaults["monetary_value_currency"] = "monetary_value_currency"
    defaults["botanical_name"] = "botanical_name"
    defaults.update(**kwargs)
    return Crop.objects.create(**defaults)


def create_fieldcultivation(**kwargs):
    defaults = {}
    defaults["duration_unit"] = "duration_unit"
    defaults["duration_of_use"] = "duration_of_use"
    defaults.update(**kwargs)
    return FieldCultivation.objects.create(**defaults)


def create_samplebase(**kwargs):
    defaults = {}
    defaults["source_certificate"] = "source_certificate"
    defaults["received_time"] = "received_time"
    defaults["concentration"] = "concentration"
    defaults["weight_unit"] = "weight_unit"
    defaults["recieved_date"] = "recieved_date"
    defaults["volume"] = "volume"
    defaults["analysis_date"] = "analysis_date"
    defaults["comment"] = "comment"
    defaults["description"] = "description"
    defaults["information_source"] = "information_source"
    defaults["volume_unit"] = "volume_unit"
    defaults["analysis_time"] = "analysis_time"
    defaults["weight"] = "weight"
    defaults["composition"] = "composition"
    defaults.update(**kwargs)
    return SampleBase.objects.create(**defaults)


def create_soilsample(**kwargs):
    defaults = {}
    defaults["soil_texture"] = "soil_texture"
    defaults["analysis_method"] = "analysis_method"
    defaults["soil_heaviness"] = "soil_heaviness"
    defaults["soil_name"] = "soil_name"
    defaults["spatial_data"] = "spatial_data"
    defaults["reference_part_of_field"] = "reference_part_of_field"
    defaults["soil_nutrient_classification"] = "soil_nutrient_classification"
    defaults["depth_range"] = "depth_range"
    defaults["soil_type"] = "soil_type"
    defaults["depth_unit"] = "depth_unit"
    defaults["depth"] = "depth"
    defaults.update(**kwargs)
    return SoilSample.objects.create(**defaults)


def create_recordedstatus(**kwargs):
    defaults = {}
    defaults["status_date"] = "status_date"
    defaults["status_time"] = "status_time"
    defaults.update(**kwargs)
    return RecordedStatus.objects.create(**defaults)


def create_harvest(**kwargs):
    defaults = {}
    defaults["quantity_unit"] = "quantity_unit"
    defaults["harvested_quantity"] = "harvested_quantity"
    defaults["harvest_quality"] = "harvest_quality"
    defaults["end_date"] = "end_date"
    defaults["yield_quantity"] = "yield_quantity"
    defaults["start_date"] = "start_date"
    defaults.update(**kwargs)
    return Harvest.objects.create(**defaults)


def create_analysisresult(**kwargs):
    defaults = {}
    defaults["parameters"] = "parameters"
    defaults["method"] = "method"
    defaults["comment"] = "comment"
    defaults["description"] = "description"
    defaults["abstract_analysis"] = "abstract_analysis"
    defaults.update(**kwargs)
    return AnalysisResult.objects.create(**defaults)


def create_programmeperformance(**kwargs):
    defaults = {}
    defaults["event_coverage"] = "event_coverage"
    defaults["programme_activities"] = "programme_activities"
    defaults["comments"] = "comments"
    defaults["participants"] = "participants"
    defaults["learning_points"] = "learning_points"
    defaults["participant_suggestions"] = "participant_suggestions"
    defaults["recommendations"] = "recommendations"
    defaults.update(**kwargs)
    return ProgrammePerformance.objects.create(**defaults)


def create_fertilizer(**kwargs):
    defaults = {}
    defaults["fertilizer_type"] = "fertilizer_type"
    defaults["fertlizer_name"] = "fertlizer_name"
    defaults["fertilizer_brand"] = "fertilizer_brand"
    defaults["fertilizer_form"] = "fertilizer_form"
    defaults.update(**kwargs)
    return Fertilizer.objects.create(**defaults)


def create_farmfield(**kwargs):
    defaults = {}
    defaults["area"] = "area"
    defaults["field_identification"] = "field_identification"
    defaults["area_unit"] = "area_unit"
    defaults["unique_area_id"] = "unique_area_id"
    defaults["name_of_field"] = "name_of_field"
    defaults["part_of_farm"] = "part_of_farm"
    defaults.update(**kwargs)
    return FarmField.objects.create(**defaults)


def create_genericstatus(**kwargs):
    defaults = {}
    defaults["status_name"] = "status_name"
    defaults["meaning"] = "meaning"
    defaults["staus"] = "staus"
    defaults.update(**kwargs)
    return GenericStatus.objects.create(**defaults)


def create_cropgrowthstage(**kwargs):
    defaults = {}
    defaults["time_recorded"] = "time_recorded"
    defaults["growth_stage"] = "growth_stage"
    defaults["date_recorded"] = "date_recorded"
    defaults["observer"] = "observer"
    defaults.update(**kwargs)
    return CropGrowthStage.objects.create(**defaults)


def create_cropspecies(**kwargs):
    defaults = {}
    defaults["genetically_modified_organism"] = "genetically_modified_organism"
    defaults["variety"] = "variety"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return CropSpecies.objects.create(**defaults)


def create_measuredkpi(**kwargs):
    defaults = {}
    defaults["impact_assessment"] = "impact_assessment"
    defaults.update(**kwargs)
    return MeasuredKPI.objects.create(**defaults)


def create_landuse(**kwargs):
    defaults = {}
    defaults["land_use_type"] = "land_use_type"
    defaults["farming_attribute"] = "farming_attribute"
    defaults["land_use_restriction_type"] = "land_use_restriction_type"
    defaults["land_use"] = "land_use"
    defaults.update(**kwargs)
    return LandUse.objects.create(**defaults)


def create_contamination(**kwargs):
    defaults = {}
    defaults["contamination_degree"] = "contamination_degree"
    defaults["noticed_date"] = "noticed_date"
    defaults["contaimination_type"] = "contaimination_type"
    defaults["noticed_time"] = "noticed_time"
    defaults.update(**kwargs)
    return Contamination.objects.create(**defaults)


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
            "start_date": "start_date",
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
            "start_date": "start_date",
            "expiry_date": "expiry_date",
        }
        url = reverse('agro_app_certificationvalidity_update', args=[certificationvalidity.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProgramPerformanceViewTest(unittest.TestCase):
    '''
    Tests for ProgramPerformance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_programperformance(self):
        url = reverse('agro_app_programperformance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_programperformance(self):
        url = reverse('agro_app_programperformance_create')
        data = {
            "participants": "participants",
            "program_activities": "program_activities",
            "comments": "comments",
            "learning_points": "learning_points",
            "recommendations": "recommendations",
            "participants_suggestions": "participants_suggestions",
            "event_coverage": "event_coverage",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_programperformance(self):
        programperformance = create_programperformance()
        url = reverse('agro_app_programperformance_detail', args=[programperformance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_programperformance(self):
        programperformance = create_programperformance()
        data = {
            "participants": "participants",
            "program_activities": "program_activities",
            "comments": "comments",
            "learning_points": "learning_points",
            "recommendations": "recommendations",
            "participants_suggestions": "participants_suggestions",
            "event_coverage": "event_coverage",
        }
        url = reverse('agro_app_programperformance_update', args=[programperformance.pk,])
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
        }
        url = reverse('agro_app_weather_update', args=[weather.pk,])
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
        }
        url = reverse('agro_app_agrodocument_update', args=[agrodocument.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


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
            "name": "name",
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
            "name": "name",
        }
        url = reverse('agro_app_farm_update', args=[farm.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CertificateViewTest(unittest.TestCase):
    '''
    Tests for Certificate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_certificate(self):
        url = reverse('agro_app_certificate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_certificate(self):
        url = reverse('agro_app_certificate_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_certificate(self):
        certificate = create_certificate()
        url = reverse('agro_app_certificate_detail', args=[certificate.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_certificate(self):
        certificate = create_certificate()
        data = {
            "name": "name",
        }
        url = reverse('agro_app_certificate_update', args=[certificate.slug,])
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
            "application_measured_unit": "application_measured_unit",
            "application_quantity": "application_quantity",
            "substance_contained": "substance_contained",
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
            "application_measured_unit": "application_measured_unit",
            "application_quantity": "application_quantity",
            "substance_contained": "substance_contained",
        }
        url = reverse('agro_app_fertilizationrecommendation_update', args=[fertilizationrecommendation.pk,])
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
            "activity": "activity",
            "comment": "comment",
            "percentage_executed": "percentage_executed",
            "daily_end": "daily_end",
            "work_done": "work_done",
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
            "activity": "activity",
            "comment": "comment",
            "percentage_executed": "percentage_executed",
            "daily_end": "daily_end",
            "work_done": "work_done",
        }
        url = reverse('agro_app_activity_update', args=[activity.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AgriculturalProgrammeViewTest(unittest.TestCase):
    '''
    Tests for AgriculturalProgramme
    '''
    def setUp(self):
        self.client = Client()

    def test_list_agriculturalprogramme(self):
        url = reverse('agro_app_agriculturalprogramme_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_agriculturalprogramme(self):
        url = reverse('agro_app_agriculturalprogramme_create')
        data = {
            "comments": "comments",
            "end": "end",
            "targets": "targets",
            "description": "description",
            "start": "start",
            "purpose": "purpose",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_agriculturalprogramme(self):
        agriculturalprogramme = create_agriculturalprogramme()
        url = reverse('agro_app_agriculturalprogramme_detail', args=[agriculturalprogramme.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_agriculturalprogramme(self):
        agriculturalprogramme = create_agriculturalprogramme()
        data = {
            "comments": "comments",
            "end": "end",
            "targets": "targets",
            "description": "description",
            "start": "start",
            "purpose": "purpose",
        }
        url = reverse('agro_app_agriculturalprogramme_update', args=[agriculturalprogramme.pk,])
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
            "cultural_name": "cultural_name",
            "monetary_value_per_hectar": "monetary_value_per_hectar",
            "description": "description",
            "monetary_value_currency": "monetary_value_currency",
            "botanical_name": "botanical_name",
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
            "cultural_name": "cultural_name",
            "monetary_value_per_hectar": "monetary_value_per_hectar",
            "description": "description",
            "monetary_value_currency": "monetary_value_currency",
            "botanical_name": "botanical_name",
        }
        url = reverse('agro_app_crop_update', args=[crop.pk,])
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
            "duration_unit": "duration_unit",
            "duration_of_use": "duration_of_use",
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
            "duration_unit": "duration_unit",
            "duration_of_use": "duration_of_use",
        }
        url = reverse('agro_app_fieldcultivation_update', args=[fieldcultivation.pk,])
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
            "source_certificate": "source_certificate",
            "received_time": "received_time",
            "concentration": "concentration",
            "weight_unit": "weight_unit",
            "recieved_date": "recieved_date",
            "volume": "volume",
            "analysis_date": "analysis_date",
            "comment": "comment",
            "description": "description",
            "information_source": "information_source",
            "volume_unit": "volume_unit",
            "analysis_time": "analysis_time",
            "weight": "weight",
            "composition": "composition",
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
            "source_certificate": "source_certificate",
            "received_time": "received_time",
            "concentration": "concentration",
            "weight_unit": "weight_unit",
            "recieved_date": "recieved_date",
            "volume": "volume",
            "analysis_date": "analysis_date",
            "comment": "comment",
            "description": "description",
            "information_source": "information_source",
            "volume_unit": "volume_unit",
            "analysis_time": "analysis_time",
            "weight": "weight",
            "composition": "composition",
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
            "soil_texture": "soil_texture",
            "analysis_method": "analysis_method",
            "soil_heaviness": "soil_heaviness",
            "soil_name": "soil_name",
            "spatial_data": "spatial_data",
            "reference_part_of_field": "reference_part_of_field",
            "soil_nutrient_classification": "soil_nutrient_classification",
            "depth_range": "depth_range",
            "soil_type": "soil_type",
            "depth_unit": "depth_unit",
            "depth": "depth",
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
            "soil_texture": "soil_texture",
            "analysis_method": "analysis_method",
            "soil_heaviness": "soil_heaviness",
            "soil_name": "soil_name",
            "spatial_data": "spatial_data",
            "reference_part_of_field": "reference_part_of_field",
            "soil_nutrient_classification": "soil_nutrient_classification",
            "depth_range": "depth_range",
            "soil_type": "soil_type",
            "depth_unit": "depth_unit",
            "depth": "depth",
        }
        url = reverse('agro_app_soilsample_update', args=[soilsample.pk,])
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
        }
        url = reverse('agro_app_recordedstatus_update', args=[recordedstatus.pk,])
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
            "quantity_unit": "quantity_unit",
            "harvested_quantity": "harvested_quantity",
            "harvest_quality": "harvest_quality",
            "end_date": "end_date",
            "yield_quantity": "yield_quantity",
            "start_date": "start_date",
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
            "quantity_unit": "quantity_unit",
            "harvested_quantity": "harvested_quantity",
            "harvest_quality": "harvest_quality",
            "end_date": "end_date",
            "yield_quantity": "yield_quantity",
            "start_date": "start_date",
        }
        url = reverse('agro_app_harvest_update', args=[harvest.pk,])
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
            "parameters": "parameters",
            "method": "method",
            "comment": "comment",
            "description": "description",
            "abstract_analysis": "abstract_analysis",
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
            "parameters": "parameters",
            "method": "method",
            "comment": "comment",
            "description": "description",
            "abstract_analysis": "abstract_analysis",
        }
        url = reverse('agro_app_analysisresult_update', args=[analysisresult.pk,])
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
            "event_coverage": "event_coverage",
            "programme_activities": "programme_activities",
            "comments": "comments",
            "participants": "participants",
            "learning_points": "learning_points",
            "participant_suggestions": "participant_suggestions",
            "recommendations": "recommendations",
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
            "event_coverage": "event_coverage",
            "programme_activities": "programme_activities",
            "comments": "comments",
            "participants": "participants",
            "learning_points": "learning_points",
            "participant_suggestions": "participant_suggestions",
            "recommendations": "recommendations",
        }
        url = reverse('agro_app_programmeperformance_update', args=[programmeperformance.pk,])
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
            "fertilizer_type": "fertilizer_type",
            "fertlizer_name": "fertlizer_name",
            "fertilizer_brand": "fertilizer_brand",
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
            "fertilizer_type": "fertilizer_type",
            "fertlizer_name": "fertlizer_name",
            "fertilizer_brand": "fertilizer_brand",
            "fertilizer_form": "fertilizer_form",
        }
        url = reverse('agro_app_fertilizer_update', args=[fertilizer.pk,])
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
            "area": "area",
            "field_identification": "field_identification",
            "area_unit": "area_unit",
            "unique_area_id": "unique_area_id",
            "name_of_field": "name_of_field",
            "part_of_farm": "part_of_farm",
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
            "area": "area",
            "field_identification": "field_identification",
            "area_unit": "area_unit",
            "unique_area_id": "unique_area_id",
            "name_of_field": "name_of_field",
            "part_of_farm": "part_of_farm",
        }
        url = reverse('agro_app_farmfield_update', args=[farmfield.pk,])
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
            "status_name": "status_name",
            "meaning": "meaning",
            "staus": "staus",
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
            "status_name": "status_name",
            "meaning": "meaning",
            "staus": "staus",
        }
        url = reverse('agro_app_genericstatus_update', args=[genericstatus.pk,])
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
            "time_recorded": "time_recorded",
            "growth_stage": "growth_stage",
            "date_recorded": "date_recorded",
            "observer": "observer",
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
            "time_recorded": "time_recorded",
            "growth_stage": "growth_stage",
            "date_recorded": "date_recorded",
            "observer": "observer",
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
            "genetically_modified_organism": "genetically_modified_organism",
            "variety": "variety",
            "name": "name",
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
            "genetically_modified_organism": "genetically_modified_organism",
            "variety": "variety",
            "name": "name",
        }
        url = reverse('agro_app_cropspecies_update', args=[cropspecies.pk,])
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
            "impact_assessment": "impact_assessment",
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
            "impact_assessment": "impact_assessment",
        }
        url = reverse('agro_app_measuredkpi_update', args=[measuredkpi.pk,])
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
            "land_use_type": "land_use_type",
            "farming_attribute": "farming_attribute",
            "land_use_restriction_type": "land_use_restriction_type",
            "land_use": "land_use",
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
            "land_use_type": "land_use_type",
            "farming_attribute": "farming_attribute",
            "land_use_restriction_type": "land_use_restriction_type",
            "land_use": "land_use",
        }
        url = reverse('agro_app_landuse_update', args=[landuse.pk,])
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
            "contamination_degree": "contamination_degree",
            "noticed_date": "noticed_date",
            "contaimination_type": "contaimination_type",
            "noticed_time": "noticed_time",
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
            "contamination_degree": "contamination_degree",
            "noticed_date": "noticed_date",
            "contaimination_type": "contaimination_type",
            "noticed_time": "noticed_time",
        }
        url = reverse('agro_app_contamination_update', args=[contamination.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


