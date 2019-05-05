from django.db import models
from django.db.models import CharField, ForeignKey
from django.contrib.contenttypes.fields import GenericRelation

	
class Animal(BaseModel):    
	identifier = CharField(unique=True, **name_default)    
	parternal_parent = ForeignKey('self', on_delete=models.DO_NOTHING)
	maternal_parent = ForeignKey('self', on_delete=models.DO_NOTHING)
	uuid = UUIDField(editable=False, default=generate_uuid)
	species = GenericRelation('farming.Species', related_query_name='animal') # @todo: implement in crop
	animal_group = GenericRelation('farming.Grouping', related_query_name='animal')
	growth_stage = GenericRelation('agric_programme.GrowthStage', related_query_name='animal')
	administered_treatment  = GenericRelation('health.TreatmentAdministration', related_query_name='animal')
	infections = GenericRelation('health.InfectedPatient', related_query_name='animal')	

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('animal_husbandry:animal:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('animal_husbandry:animal:update', args=(self.pk,))
		

class AnimalRearing(BaseModel):
	farm_field = ForeignKey('farming.FarmField')
	cultivation = ForeignKey('farming.Cultivation')		
	animal = ManyToManyField('animal_husbandry.Animal')
		

class AnimalHarvest(Harvest):	
	animal = ForeignKey('animal_husbandry.Animal')	
	
	class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('animal_husbandry:animal_harvest:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('animal_husbandry:animal_harvest:update', args=(self.pk,))


		
class Feed(BaseModel):	
    composition = TextField(**text_default)
    general_name = CharField(**name_default)
    manufacturer_name = CharField(**name_default)
    manufacturer = CharField(**char_default)
    feed_texture = TextField(**text_default)
    description = TextField(**text_default)
    feed_channel = CharField(**code_default)
    
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('animal_husbandry:feed:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('animal_husbandry:feed:update', args=(self.pk,))

class FeedAdministration(models.Model):	
	quantity_disbursed = DecimalField(**decimal_default)
    feeding_location = CharField(**char_default)
    feeding_conditions = TextField(**text_default)
    animal_fed = ManyToManyField(Feed, on_delete=models.DO_NOTHING)
    group_animal_fed = ForeignKey(Grouping, null=True)
	
	def save(self, *args, **kwargs):
		# ensure only group_animal_fed or animal_fed is set for each record.
		# animal_fed and group_animal_fed are mutually exclusive
		pass



class AnimalBreeder(BaseModel):    
    quantity = IntegerField()
    acquisition_cost = DecimalField(**decimal_default)
    target_harvest_date = DateField(**date_default)
    target_harvest_quantity = DecimalField(**decimal_default)
    target_harvest_value = DecimalField(**decimal_default)
    species = ForeignKey('farming.Species', on_delete=models.CASCADE, related_name="breeders")

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('animal_husbandry:animal_breeder:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('animal_husbandry:animal_breeder:update', args=(self.pk,))

	