# Farm models

class BaseModel(models.Model):
	# Done
	created_at = DateTimeField(auto_now_add=True)
	last_modified_at = DateField(auto_now=True)
	deleted_at = DateTimeField(auto_now_add=False, auto_now=False)
	enable_soft_delete = BooleanField(default=True)
	force_delete = BooleanField(default=False)
	
	def save(self, *args, **kwargs):
		# apply the soft delete concept on save
		pass
		
	def delete(self, *args, **kwargs):
		# apply the soft delete concept on delete
		# if force_delete = True, then delete from db irrespective of settings
		pass
	
	class Meta:
		abstract = True
		
		
class Event(BaseModel):    
	# Done
    event_comment = TextField(**text_default)
    event_start = DateTimeField(**date_default)    
    event_end = DateTimeField(**date_default)    
    observer = ForeignKey(User, on_delete=models.CASCADE, related_name="event_observer",) # defaults to user reporting event
    performer = ForeignKey(User, on_delete=models.CASCADE, related_name="events_performer", null=True)

    class Meta:
        abstract = True

		
class Signatures:
    # Done
	document = ManyToManyField('AgroDocument')
	hash = CharField()
	binary_hash = BinaryField()
	signature_timestamp = DateTimeField()

	
class AgroDocument(BaseModel):
	# Done
	receiving_party = ForeignKey(User, on_delete=models.DO_NOTHING)
	sending_party = ForeignKey(User, on_delete=models.DO_NOTHING)
	description = TextField()
	issue_date = DateField()
	issue_time = TimeField()
	revision_date = DateField()
	revision_time = TimeField()		
	version_id = CharField(default=version_id_generator, editable=False)	
	
    class Meta:        
		abstract = True	
		
class NamedCode(models.Model):
	# Done
	# The name or string repr which can be parsed by target enum type.
	# The enum will have a default OTHER for cases not yet identified
	# Enum flag OTHER will enable collection and processing 
	name = CharField(**name_default)
	code_value = CharField(**text_default)
	meaning = TextField()
	
	def parse_to_enum(self, name, value=None, enum_type=None):
		# return a given enum member for the given (name, value) pair in model record
		pass
		
	def parse_from_enum(self, enum_type=None, enum_value=None, enum_name=None):
		pass
	

class GenericStatus(NamedCodes):
    # Done
	def save(self, *args, **kwargs):
		# ensure only codes from the status enum are saved
		pass

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_genericstatus_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_genericstatus_update', args=(self.pk,))
		
		
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

		
class AgriculturalProgramme(models.Model):
	# Done
    comments = TextField()    
    targets = TextField()
    description = TextField()
    programme_start = DateTimeField()		
	programme_end = DateTimeField()
    purpose = TextField()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_agriculturalprogramme_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_agriculturalprogramme_update', args=(self.pk,))
		
class ProgrammePerformance(Model):
	# Done
	participants = ManyToManyField(User, through='Participation') # actual record of participants as against invitation            
	programme = ForeignKey(AgriculturalProgramme, on_delete=models.CASCADE)
	programme_activities = ManyToManyField('Activity')  # reference the generic activity model	
	learning_points = TextField(**text_default)  # learning from the event by organisers
	recommendations = CharField(**text_default)  # should hold organisers recommendations for later
	event_coverage = FileField()  # uploaded photos or videos

class Participation(models.Model):
	# Done
	programme_performance = ForeignKey(ProgrammePerformance)
	participant = ForeignKey(User)
	participant_suggestions = CharField(**text_default)  # should hold participants suggestions/recommendations
	recommendations = CharField(**text_default)  # should hold organisers recommendations for later	
	comments = TextField(**text_default)
	participant_coverage = FileField()
	
	
class MeasuredKPI(Model):
	# Done
	measured_kpis = JSONField(**name_default)  # delimited name for the KPIs measured with their unit
	impact_assessment = TextField(**text_default)
	programme = ForeignKey('AgriculturalProgramme')
	
class Treatment(BaseModel):	
	# Done
    treatment_type = CharField(**code_default)    
    health_worker = ForeignKey(
        'agro_farm_monitoring.User',
        on_delete=models.DO_NOTHING, related_name="treatments", 
    )
	treatment_administration = ForeignKey('TreatmentAdministration')
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_treatment_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_treatment_update', args=(self.pk,))
		

class Infection(BaseModel):
    # Done
    medical_name = CharField(**name_default)
    cultural_name = CharField(**name_default)
    infection_code = CharField(**code_default)
    description = TextField(**text_default)    
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_infection_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_infection_update', args=(self.pk,))

class InfectedPatient(BaseModel):
	# Done
	noticed_datetime = DateTimeField()
	contamination_degree = TextField()
	content_object = GenericForeignKey()
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = PositiveIntegerField
	
	class Meta:
		abstract = True		

		
class TreatmentAdministration(BaseModel):
	# Done
    drug = CharField(**name_default)
    drug_type = CharField(**code_default)
    drug_administered_as = CharField(**code_default)
    treatment = ForeignKey(
        'agro_farm_monitoring.Treatment',
        on_delete=models.CASCADE, related_name="treatmentadministrations", 
    )
	content_object = GenericForeignKey()
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = PositiveIntegerField()
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_treatmentadministration_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_treatmentadministration_update', args=(self.pk,))
		
	class Meta:
		abstract = True
		
class FarmCertificate(models.Model):
	# Done
    certificate_name = models.CharField(max_length=255)    
	certificate_number = CharField(**name_default)
	issuer = CharField(**name_default)
	recipient = ForeignKey(User, null=True)  # owner/representative of the farm
	issue_date = DateField()
	expiry_date = DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)  
	farm = ForeignKey('Farm', on_delete=models.CASCADE)
	
    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('agro_app_certificate_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('agro_app_certificate_update', args=(self.slug,))
		
	def save(self, *args, **kwargs):
		# certificate should not be updated only created
		pass


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
		
		
class Grouping(BaseModel):
	# manage animals or plants in groups. E.g herds of cattle
	group_name = CharField(**name_default)
	max_member_count = PositiveIntegerField()
	min_member_count = PositiveIntegerField()
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = PositiveIntegerField()
	content_object = GenericForeignKey()	
	
class Inventory(BaseModel):
	# Done
	reorder_level = IntegerField(default=0)
	reorder_quantity = IntegerField(default=0)
	details = JSONField()	
	object_id = PositiveIntegerField()
	asset = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('asset', 'object_id')	
		
class StockTaking(Event):
	# Done
	quantity = IntegerField
	inventory = ForeignKey(Inventory)
	
class FarmProduce(BaseModel):
	# Done
	product_name = CharField(**name_default)
	cultural_name = CharField(**name_default)
    brand_name = CharField(**name_default)
    estimated_value = DecimalField(**decimal_default)
    market_value = DecimalField(**decimal_default)
    product_code = CharField(**code_default)

class CatalogueProduct(BaseModel):
    # Done           
	object_id = PositiveIntegerField()
	source = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('source', 'object_id')
    product = ForeignKey(FarmProduce, on_delete=models.CASCADE, related_name='farm_produce')

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_animalproduct_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_animalproduct_update', args=(self.pk,))

class ProgramPerformance(Event):
	# Done
    participants = models.TextField(**text_default)
    program_activities = models.TextField(**text_default)
    learning_points = models.TextField(**text_default)
    recommendations = models.TextField(**text_default)
    participants_suggestions = models.TextField(**text_default)    

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_programperformance_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_programperformance_update', args=(self.pk,))
		
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


class DailyTask(Event):
	# Done
	activity = ForeignKey('Activity', on_delete=models.CASCADE)
	description = TextField()
	assigned_to = CharField(**name_default)  # identifier or name of the staff assigned
	performance_started_at = DateTimeField()  # the date and time the task was performed
	performance_ended_at = DateTimeField()
	status = CharField(**code_default)

class Activity(BaseModel):
	# Done    
	activity = TextField()
    comment = TextField()
    percentage_executed = DecimalField(**decimal_default)    
    work_done = TextField()
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_activity_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('agro_app_activity_update', args=(self.pk,))