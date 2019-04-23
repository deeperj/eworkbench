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


