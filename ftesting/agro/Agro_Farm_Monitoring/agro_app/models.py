from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from  import BinaryField
from  import BooleanField
from  import CharField
from  import DateField
from  import DateTimeField
from  import DateTimefield
from  import DecimalField
from  import TimeField
from  import UUIDField
from model import CharField
from model import DateField
from models import CharField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Farm(models.Model):

    # Fields
    description = CharField(**default_char)
    purpose = CharField(**default_char)
    farming_system = CharField(**default_char)

    # Relationship Fields
    owner = ForeignKey(
        'agro_app.User',
        on_delete=models.CASCADE, related_name="farms", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farm_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_farm_update', args=(self.pk,))


class FarmCertificate(models.Model):

    # Fields
    first_certificate_date = DateField(**default_date)
    certification_agency = CharField(**default_char)
    certificate_number = UUIDField()
    certification_code = CharField(**default_code)
    supporting_documents = BinaryField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farmcertificate_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_farmcertificate_update', args=(self.pk,))


class CertificationValidity(models.Model):

    # Fields
    valid_for_purpose = BooleanField(**bool_default)
    farm_purpose = CharField(**default_char)
    issue_date = DateField(**default_date)
    expiry_date = DateField(**default_date)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_certificationvalidity_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_certificationvalidity_update', args=(self.pk,))


class FarmField(models.Model):

    # Fields
    name_of_field = CharField(**name_default)
    field_identification = UUIDField()
    unique_area_id = UUIDField()
    area = DecimalField(**number_default)
    area_unit = CharField(**code_default)
    spatial_data = CharField(**text_default)

    # Relationship Fields
    cultivation = ForeignKey(
        'agro_app.Cultivation',
        on_delete=models.CASCADE, related_name="farmfields", 
    )
    land_use_restriction = ForeignKey(
        'agro_app.LandUse',
        on_delete=models.CASCADE, related_name="farmfields", 
    )
    assessment = ForeignKey(
        'agro_app.Assessment',
        on_delete=models.CASCADE, related_name="farmfields", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farmfield_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_farmfield_update', args=(self.pk,))


class Assessment(models.Model):


    # Relationship Fields
    analysis = ForeignKey(
        'agro_app.Analysis',
        on_delete=models.CASCADE, related_name="assessments", 
    )
    status = ForeignKey(
        'agro_app.RecordedStatus',
        on_delete=models.CASCADE, related_name="assessments", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_assessment_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_assessment_update', args=(self.pk,))


class GenericStatus(models.Model):

    # Fields
    staus = CharField(**code_default)
    status_name = CharField(**name_default)
    meaning = CharField(**text_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_genericstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_genericstatus_update', args=(self.pk,))


class RecordedStatus(models.Model):

    # Fields
    status_date = DateField(**date_default)
    status_time = TimeField(**time_default)

    # Relationship Fields
    status = ForeignKey(
        'agro_app.GenericStatus',
        on_delete=models.CASCADE, related_name="recordedstatuss", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_recordedstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_recordedstatus_update', args=(self.pk,))


class LandUse(models.Model):

    # Fields
    land_use_restriction_type = CharField(**code_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_landuse_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_landuse_update', args=(self.pk,))


class FertilizationRecommendation(models.Model):



    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizationrecommendation_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fertilizationrecommendation_update', args=(self.pk,))


class SampleBase(models.Model):

    # Fields
    recieved_date = DateField(**date_default)
    received_time = TimeField(**number_default)
    description = CharField(**text_default)
    comment = CharField(**text_default)
    weight = DecimalField(**number_default)
    weight_unit = CharField(**code_default)
    volume = DecimalField(**number_default)
    volume_unit = CharField(**code_default)
    analysis_date = DateField(**date_default)
    analysis_time = TimeField(**number_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_samplebase_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_samplebase_update', args=(self.pk,))


class SoilSample(models.Model):

    # Fields
    soil_name = CharField(**text_default)  # Give alternative CharField(**name_default) to soil type where not available in CharField(**code_default)
    soil_type = CharField(**code_default)
    reference_part_of_field = CharField(**text_default)
    spatial_data = CharField(**text_default)
    depth = DecimalField(**number_default)
    depth_unit = CharField(**code_default)
    depth_range = CharField(**text_default)
    analysis_method = CharField(**text_default)
    soil_heaviness = CharField(**text_default)
    soil_nutrient_classification = CharField(**text_default)
    soil_texture = CharField(**text_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_soilsample_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_soilsample_update', args=(self.pk,))


class AnalysisResult(models.Model):

    # Fields
    abstract_analysis = CharField(**text_default)
    description = CharField(**text_default)
    method = CharField(**text_default)
    comment = CharField(**text_default)

    # Relationship Fields
    sample = ForeignKey(
        'agro_app.ReportedSample',
        on_delete=models.CASCADE, related_name="analysisresults", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_analysisresult_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_analysisresult_update', args=(self.pk,))


class Fertilizer(models.Model):

    # Fields
    fertilizer_brand = CharField(**text_default)  # general market brand CharField(**name_default)
    fertlizer_name = CharField(**text_default)  # specific manufacturer CharField(**name_default)
    fertilizer_type = CharField(**code_default)
    fertilizer_form = CharField(**text_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fertilizer_update', args=(self.pk,))


class FieldCultivation(models.Model):

    # Fields
    duration_of_use = DecimalField(**number_default)
    duration_unit = CharField(**code_default)

    # Relationship Fields
    farm_field = ForeignKey(
        'agro_app.FarmField',
        on_delete=models.CASCADE, related_name="fieldcultivations", 
    )
    reference_field_part = ForeignKey(
        'agro_app.FarmField',
        on_delete=models.CASCADE, related_name="fieldcultivations_2", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fieldcultivation_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fieldcultivation_update', args=(self.pk,))


class Crop(models.Model):

    # Fields
    monetary_value_per_hectar = DecimalField(**number_default)
    monetary_value_currency = CharField(**code_default)
    botanical_name = CharField(**name_default)

    # Relationship Fields
    farm_field = ForeignKey(
        'agro_app.FarmField',
        on_delete=models.CASCADE, related_name="crops", 
    )
    crop_growth_event = ForeignKey(
        'agro_app.CropGrowthStage',
        on_delete=models.CASCADE, related_name="crops", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_crop_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_crop_update', args=(self.pk,))


class CropGrowthStage(models.Model):

    # Fields
    growth_stage = CharField(**text_default)
    date_recorded = DateField(**date_default)
    time_recorded = TimeField(**number_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_cropgrowthstage_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_cropgrowthstage_update', args=(self.pk,))


class CropSpecies(models.Model):

    # Fields
    name = CharField(**name_default)
    variety = CharField(**code_default)
    genetically_modified_organism = BooleanField(**bool_default)

    # Relationship Fields
    crop = ForeignKey(
        'agro_app.Crop',
        on_delete=models.CASCADE, related_name="cropspeciess", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_cropspecies_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_cropspecies_update', args=(self.pk,))


class Harvest(models.Model):

    # Fields
    harvested_quantity = DecimalField(**number_default)
    yield_quantity = DecimalField(**number_default)
    quantity_unit = CharField(**code_default)
    harvest_quality = CharField(**code_default)
    start_date = DateField(**date_default)
    end_date = DateField(**date_default)

    # Relationship Fields
    crop = ForeignKey(
        'agro_app.Crop',
        on_delete=models.CASCADE, related_name="harvests", 
    )
    farm_field = ForeignKey(
        'agro_app.FarmField',
        on_delete=models.CASCADE, related_name="harvests", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_harvest_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_harvest_update', args=(self.pk,))


class Activity(models.Model):

    # Fields
    daily_start = DateTimefield(**datetime_default)
    daily_end = DateTimefield(**datetime_default)
    activity = CharField(**text_default)
    comment = CharField(**text_default)
    work_done = CharField(**text_default)
    percentage_executed = DecimalField(**number_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_activity_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_activity_update', args=(self.pk,))


class Weather(models.Model):

    # Fields
    temperature = DecimalField(**number_default)
    temperature_unit = CharField(**code_default)
    wind_speed = DecimalField(**number_default)
    wind_speed_unit = CharField(**code_default)
    humidity = DecimalField(**number_default)
    humidity_unit = CharField(**code_default)
    precipitation = DecimalField(**number_default)
    precipitation_unit = CharField(**code_default)
    solar_radiation = DecimalField(**number_default)
    solar_radiation_unit = CharField(**code_default)
    reported_date = DateField(**date_default)
    reported_time = TimeField(**number_default)
    measured_date = DateField(**date_default)
    measured_time = TimeField(**number_default)

    # Relationship Fields
    reported_by = ForeignKey(
        'agro_app.User',
        on_delete=models.CASCADE, related_name="weathers", 
    )
    measured_by = ForeignKey(
        'agro_app.User',
        on_delete=models.CASCADE, related_name="weathers_2", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_weather_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_weather_update', args=(self.pk,))


class Contamination(models.Model):

    # Fields
    contaimination_type = CharField(**text_default)
    contamination_degree = CharField(**text_default)
    noticed_date = DateField(**date_default)
    noticed_time = TimeField(**number_default)
    start = DateTimeField(**datetime_default)
    end = DateTimeField(**datetime_default)
    invitations = CharField(**text_default)
    consultants = CharField(**text_default)
    purpose = CharField(**text_default)
    description = CharField(**text_default)
    targets = CharField(**text_default)
    comments = CharField(**text_default)

    # Relationship Fields
    reported_by = ForeignKey(
        'agro_app.User',
        on_delete=models.CASCADE, related_name="contaminations", 
    )
    affected_fields = ForeignKey(
        'agro_app.FarmField',
        on_delete=models.CASCADE, related_name="contaminations", 
    )
    kpis = ForeignKey(
        'agro_app.MeasuredKPI',
        on_delete=models.CASCADE, related_name="contaminations", 
    )
    status = ForeignKey(
        'agro_app.RecordedStatus',
        on_delete=models.CASCADE, related_name="contaminations", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_contamination_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_contamination_update', args=(self.pk,))


class ProgrammePerformance(models.Model):

    # Fields
    comments = CharField(**text_default)
    learning_points = CharField(**text_default)
    recommendations = CharField(**text_default)
    participant_suggestions = CharField(**text_default)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_programmeperformance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_programmeperformance_update', args=(self.pk,))


class MeasuredKPI(models.Model):

    # Fields
    measured_kpis = CharField(**name_default)
    impact_assessment = CharField(**text_default)

    # Relationship Fields
    programme_performance = ForeignKey(
        'agro_app.ProgrammePerformance',
        on_delete=models.CASCADE, related_name="measuredkpis", 
    )
    fertilizer = ForeignKey(
        'agro_app.Fertilizer',
        on_delete=models.CASCADE, related_name="measuredkpis", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_measuredkpi_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_measuredkpi_update', args=(self.pk,))


class AgroDocument(models.Model):

    # Fields
    profile = CharField(**default_char)

    # Relationship Fields
    farm = ForeignKey(
        'agro_app.Farm',
        on_delete=models.CASCADE, related_name="agrodocuments", 
    )
    work_process = ForeignKey(
        'agro_app.WokProcess',
        on_delete=models.CASCADE, related_name="agrodocuments", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_agrodocument_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_agrodocument_update', args=(self.pk,))


