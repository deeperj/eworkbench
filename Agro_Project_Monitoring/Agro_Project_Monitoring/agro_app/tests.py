import unittest
from django.urls import reverse
from django.test import Client
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate
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


