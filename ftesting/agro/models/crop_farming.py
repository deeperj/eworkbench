from agro_farm_monitoring.db import BaseModel, Event, GenericStatus, NamedCode 
from agro_farm_monitoring.farming.models GrowthStage, Farm, Harvest
from django.urls import reverse		


class Crop(BaseModel):	
	farm_field = ForeignKey('farming.FarmField')
	monetary_value_per_hectar = DecimalField(**number_default)
	monetary_value_currency = CharField(**code_default)
	growth_stage = GenericRelation('farming.GrowthStage', related_query_name='crop')
	botanical_name = CharField(**name_default)
	cultural_name = CharField(**name_default)
	description = TextField(**text_default)
	specie = GenericRelation(Species, related_query_name='crop')
	administered_treatments = GenericRelation('health.TreatmentAdministration', related_query_name='crop')
	infections = GenericRelation('health.InfectedPatient', related_query_name='crop')
	crop_group = GenericRelation(Grouping, related_query_name='crop')
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('crop_farming:crop:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('crop_farming:crop:update', args=(self.pk,))


class Cultivation(models.Model):	
    name = CharField(**name_default)
	description = TextField()
	technique = TextField()
	benefits = TextField()
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('crop_farming:cultivation:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('crop_farming:cultivation:update', args=(self.pk,))


class CropHarvest(Harvest):	
	crop = ForeignKey('Crop')		

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('crop_farming:crop_harvest:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('crop_farming:crop_harvest:update', args=(self.pk,))





