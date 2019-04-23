from django import forms
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate


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


