from django.contrib import admin
from django import forms
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate

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


