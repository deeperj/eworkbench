from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BinaryField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from models import BinaryField
from models import BooleanField
from models import CharField
from models import DateField
from models import DateTimeField
from models import IntegerField
from models import TextField
from models import TimeField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class CertificationValidity(models.Model):

    # Fields
    valid_for_purpose = models.BooleanField()
    farm_purpose = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    issue_date = models.DateField()
    start_date = models.DateField()
    expiry_date = models.DateField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_certificationvalidity_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_certificationvalidity_update', args=(self.pk,))


class ProgramPerformance(models.Model):

    # Fields
    participants = models.TextField(max_length=255)
    program_activities = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    comments = models.TextField()
    learning_points = models.TextField()
    recommendations = models.TextField()
    participants_suggestions = models.TextField()
    event_coverage = models.BinaryField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_programperformance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_programperformance_update', args=(self.pk,))


class Weather(models.Model):

    # Fields
    temperature = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    temperature_unit = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_speed_unit = models.IntegerField()
    humidity = models.IntegerField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_weather_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_weather_update', args=(self.pk,))


class AgroDocument(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_agrodocument_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_agrodocument_update', args=(self.pk,))


class Farm(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farm_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_farm_update', args=(self.pk,))


class Certificate(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('agro_app_certificate_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('agro_app_certificate_update', args=(self.slug,))


class FertilizationRecommendation(models.Model):

    # Fields
    application_measured_unit = IntegerField()
    application_quantity = IntegerField()
    substance_contained = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizationrecommendation_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fertilizationrecommendation_update', args=(self.pk,))


class Activity(models.Model):

    # Fields
    daily_start = DateTimeField()
    activity = TextField()
    comment = TextField()
    percentage_executed = IntegerField()
    daily_end = DateTimeField()
    work_done = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_activity_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_activity_update', args=(self.pk,))


class AgriculturalProgramme(models.Model):

    # Fields
    comments = TextField()
    end = DateTimeField()
    targets = TextField()
    description = TextField()
    start = DateTimeField()
    purpose = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_agriculturalprogramme_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_agriculturalprogramme_update', args=(self.pk,))


class Crop(models.Model):

    # Fields
    cultural_name = CharField()
    monetary_value_per_hectar = IntegerField()
    description = TextField()
    monetary_value_currency = IntegerField()
    botanical_name = CharField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_crop_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_crop_update', args=(self.pk,))


class FieldCultivation(models.Model):

    # Fields
    duration_unit = IntegerField()
    duration_of_use = IntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fieldcultivation_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fieldcultivation_update', args=(self.pk,))


class SampleBase(models.Model):

    # Fields
    source_certificate = TextField()
    received_time = TimeField()
    concentration = TextField()
    weight_unit = IntegerField()
    recieved_date = DateField()
    volume = IntegerField()
    analysis_date = DateField()
    comment = TextField()
    description = TextField()
    information_source = TextField()
    volume_unit = IntegerField()
    analysis_time = TimeField()
    weight = IntegerField()
    composition = TextField()


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
    soil_texture = TextField()
    analysis_method = TextField()
    soil_heaviness = TextField()
    soil_name = TextField()
    spatial_data = TextField()
    reference_part_of_field = TextField()
    soil_nutrient_classification = TextField()
    depth_range = TextField()
    soil_type = IntegerField()
    depth_unit = IntegerField()
    depth = IntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_soilsample_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_soilsample_update', args=(self.pk,))


class RecordedStatus(models.Model):

    # Fields
    status_date = DateField()
    status_time = TimeField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_recordedstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_recordedstatus_update', args=(self.pk,))


class Harvest(models.Model):

    # Fields
    quantity_unit = IntegerField()
    harvested_quantity = IntegerField()
    harvest_quality = IntegerField()
    end_date = DateField()
    yield_quantity = IntegerField()
    start_date = DateField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_harvest_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_harvest_update', args=(self.pk,))


class AnalysisResult(models.Model):

    # Fields
    parameters = TextField()
    method = TextField()
    comment = TextField()
    description = TextField()
    abstract_analysis = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_analysisresult_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_analysisresult_update', args=(self.pk,))


class ProgrammePerformance(models.Model):

    # Fields
    event_coverage = BinaryField()
    programme_activities = TextField()
    comments = TextField()
    participants = TextField()
    learning_points = TextField()
    participant_suggestions = TextField()
    recommendations = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_programmeperformance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_programmeperformance_update', args=(self.pk,))


class Fertilizer(models.Model):

    # Fields
    fertilizer_type = IntegerField()
    fertlizer_name = TextField()
    fertilizer_brand = TextField()
    fertilizer_form = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_fertilizer_update', args=(self.pk,))


class FarmField(models.Model):

    # Fields
    area = IntegerField()
    field_identification = IntegerField()
    area_unit = IntegerField()
    unique_area_id = IntegerField()
    name_of_field = CharField()
    part_of_farm = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farmfield_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_farmfield_update', args=(self.pk,))


class GenericStatus(models.Model):

    # Fields
    status_name = CharField()
    meaning = TextField()
    staus = IntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_genericstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_genericstatus_update', args=(self.pk,))


class CropGrowthStage(models.Model):

    # Fields
    time_recorded = TimeField()
    growth_stage = TextField()
    date_recorded = DateField()
    observer = TextField()


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
    genetically_modified_organism = BooleanField()
    variety = IntegerField()
    name = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_cropspecies_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_cropspecies_update', args=(self.pk,))


class MeasuredKPI(models.Model):

    # Fields
    impact_assessment = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_measuredkpi_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_measuredkpi_update', args=(self.pk,))


class LandUse(models.Model):

    # Fields
    land_use_type = IntegerField()
    farming_attribute = IntegerField()
    land_use_restriction_type = IntegerField()
    land_use = TextField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_landuse_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_landuse_update', args=(self.pk,))


class Contamination(models.Model):

    # Fields
    contamination_degree = TextField()
    noticed_date = DateField()
    contaimination_type = TextField()
    noticed_time = TimeField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_contamination_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_contamination_update', args=(self.pk,))


