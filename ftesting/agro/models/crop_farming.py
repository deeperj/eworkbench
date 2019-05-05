from . import BaseModel, Event, GenericStatus, NamedCode, Harvest, GrowthStage, Farm
		


class Crop(BaseModel):
	# Done
	farm_field = ForeignKey('FarmField')
	monetary_value_per_hectar = DecimalField(**number_default)
	monetary_value_currency = CharField(**code_default)
	growth_stage = GenericRelation('GrowthStage', related_query_name='crop')
	botanical_name = CharField(**name_default)
	cultural_name = CharField(**name_default)
	description = TextField(**text_default)
	specie = GenericRelation(Species, related_query_name='crop')
	administered_treatments = GenericRelation('TreatmentAdministration', related_query_name='crop')
	infections = GenericRelation('InfectedPatient', related_query_name='crop')
	crop_group = GenericRelation(Grouping, related_query_name='crop')
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_crop_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_crop_update', args=(self.pk,))


class Cultivation(models.Model):
	# Done
    name = CharField(**name_default)
	description = TextField()
	technique = TextField()
	benefits = TextField()
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fieldcultivation_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_fieldcultivation_update', args=(self.pk,))


class CropHarvest(Harvest):
	# Done
	crop = ForeignKey('Crop')		

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_harvest_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_harvest_update', args=(self.pk,))





