from . import BaseModel

class Farm(BaseModel):
	# Done
    name = models.CharField(max_length=255)    
	farm_purpose = models.TextField()
	owner = models.ForeignKey(User)
	location = model.CharField(**default_char)  # use address type or GPS reading here
	description = model.CharField(**default_char)	
	size = model.CharField(**default_char)  # gives the calculated land size for the farm. Not necessarily sum of field area
	farming_system = model.CharField(**default_char)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_farm_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_farm_update', args=(self.pk,))
		

class FarmField(Model):	
	# Done
	name_of_field = CharField(**name_default)	
	unique_area_id = UUIDField(editable=False, default=generate_uuid)	
	area = DecimalField(**number_default)
	area_unit = CharField(**code_default)
	part_of_farm = CharField(**text_default)  # represent a named region in the farm
	spatial_data = CharField(**text_default)  
	farm = ForeignKey(Farm, on_delete=models.CASCADE)
	
		
class LandUse(models.Model):
	# Done
    land_use_type = CharField(**code_default) # crop, animal, storage, processing farm usage
    land_use_restriction_type = CharField()
    land_use = TextField()
	farm_field = ForeignKey('FarmField', on_delete=models.DO_NOTHING)
	duration_of_use = DurationField()
	duration_unit = CharField(**code_default) 

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_landuse_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_landuse_update', args=(self.pk,))

class Harvest(BaseModel):
	# Done
	harvested_quantity = DecimalField(**number_default)
	yield_quantity = DecimalField(**number_default)
	quantity_unit = CharField(**code_default)
	harvest_quality = CharField(**code_default)
	start_date = DateField(**date_default)
	end_date = DateField(**date_default)
	harvest_field = ForeignKey('FarmField', on_delete=DO_NOTHING)
	
	class Meta:
		abstract = True
		
class Species(models.Model):
	# Done
	# provide relations to both the Animal and Crop model
	# specie = Specie(botanical_name=b, common_name=c, content_object=animal_instance)
	# specie.save()
	botanical_name = CharField(null=True, **name_default)
	common_name = CharField(null=True, **name_default)
	code = CharField(unique=True, **code_default)
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = PositiveIntegerField()
	content_object = GenericForeignKey()
	
	def __str__(self):
		return self.botanical_name


class GrowthStage(models.Model):
	# 
    recorded_at = DateTimeField()    
	growth_stage = CharField(**name_default)    
	measurements = JSONField()  # measured growth in weight, height, width etc as may be applicable for crop/animal
    observer = CharField(**name_default)
	content_object = GenericForeignKey()
	content_type = ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = PositiveIntergerField()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_cropgrowthstage_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_cropgrowthstage_update', args=(self.pk,))

class Grouping(BaseModel):
	# manage animals or plants in groups. E.g herds of cattle
	group_name = CharField(**name_default)
	max_member_count = PositiveIntegerField()
	min_member_count = PositiveIntegerField()
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = PositiveIntegerField()
	content_object = GenericForeignKey()	


class Weather(Event):
	# Done
	precipitation = DecimalField(**number_default)
	precipitation_unit = CharField(**code_default)
	solar_radiation = DecimalField(**number_default)
	solar_radiation_unit = CharField(**code_default)
	temperature = DecimalField(**decimal_default)
    temperature_unit = CharField(**code_default)
    wind_speed = DecimalField(**decimal_default)
    wind_speed_unit = CharField(**code_default)
    humidity = DecimalField(**decimal_default)
	humidity_unit = CharField(**code_default)	
	reported_date = DateField(**date_default)
	reported_time = TimeField(**number_default)
	reported_by = CharField()  # can be weather station or 3rd party agent. store identifier
	measured_date = DateField(**date_default)  # use this field for weather condition measured by on farm
	measured_time = TimeField(**number_default)	
	measured_by = CharField()  # store identifier for user    
	farm = ForeignKey(Farm)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_weather_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_weather_update', args=(self.pk,))
