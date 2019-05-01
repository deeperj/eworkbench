# @todo: a code model holding all char codes, description, meaning, integer value and possibly enum mapping
# @todo: codes should map to enum defined

	
class Animal(BaseModel):
    # Done
	identifier = CharField(unique=True, **name_default)    
	parternal_parent = ForeignKey('self', on_delete=models.DO_NOTHING)
	maternal_parent = ForeignKey('self', on_delete=models.DO_NOTHING)
	uuid = UUIDField(editable=False, default=generate_uuid)
	species = GenericRelation(Species, related_query_name='animal') # @todo: implement in crop
	animal_group = GenericRelation(Grouping, related_query_name='animal')
	growth_stage = GenericRelation(GrowthStage, related_query_name='animal')
	administered_treatment  = GenericRelation('TreatmentAdministration', related_query_name='animal')
	infections = GenericRelation('InfectedPatient', related_query_name='animal')	

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_animal_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_animal_update', args=(self.pk,))
		

class AnimalRaring():
	farm_field = ForeignKey(FarmField)
	cultivation = ForeignKey(Cultivation)		
	animal = ManyToManyField(Animal)
		
class AnimalHarvest(Harvest):
	# Done
	animal = ForeignKey('Animal')	
	
	class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_harvest_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_harvest_update', args=(self.pk,))


		
class Feed(BaseModel):
	# Done
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
        return reverse('agro_farm_monitoring_feed_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_feed_update', args=(self.pk,))

class FeedAdministration(models.Model):
	# Done
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
    # Done
    quantity = IntegerField()
    acquisition_cost = DecimalField(**decimal_default)
    target_harvest_date = DateField(**date_default)
    target_harvest_quantity = DecimalField(**decimal_default)
    target_harvest_value = DecimalField(**decimal_default)
    species = ForeignKey(Species, on_delete=models.CASCADE, related_name="breeders")

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_breeder_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_breeder_update', args=(self.pk,))

	