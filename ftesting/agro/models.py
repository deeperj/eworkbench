
char_default = {
	length: 100,
}

date_default = {
	auto_now: False, 
	auto_now_add: False, 
	options: {}
}

datetime_default = {

}

code_default = {
	
}

bool_default = {

}

name_default = {

}

text_default = {

}

options = {
	: ,
}

class AgroDocument(Model):	
	contract_number = models.UUIDField
	farm = models.ForeignKey(Farm)
	work_process = models.ForeignKey(WokProcess)            
	profile = models.CharField(**default_char)
	
	
class Farrm(Model):
	farm_fields = models.ForeignKey(FarmField)  # references the various arable regions on the farm
	CharField(**name_default) = models.CharField(**default_char)
	owner = models.ForeignKey(User)
	location = model.CharField(**default_char)  # use address type or GPS reading here
	description = model.CharField(**default_char)
	purpose = model.CharField(**default_char)
	certificate = model.ForeignKey(FarmCertificate)
	agric_programme = model.ForeignKey(AgricProgramme)
	size = model.CharField(**default_char)  # gives the calculated land mass for the farm. Not necessarily sum of field area
	farming_system = model.CharField(**default_char)


class FarmCertificate(Model):
	first_certificate_date = model.DateField(**default_date)
	certification_agency = model.CharField(**default_char)
	validity = model.ForeignKey(CertificationValidity)
	certificate_number = UUIDField()
	certification_code = CharField(**default_code)
	supporting_documents = BinaryField() 
	
	
class CertificationValidity(Model):
	valid_for_purpose = BooleanField(**bool_default)
	farm_purpose = CharField(**default_char)
	issue_date = DateField(**default_date)
	start_date = DateField(**default_date) # defaults to issue_date when not specified
	expiry_date = DateField(**default_date) 

	
class FarmField(Model):
	cultivation = ForeignKey(Cultivation)
	name_of_field = CharField(**name_default)
	field_identification = UUIDField()
	unique_area_id = UUIDField()
	area = DecimalField(**number_default)
	area_unit = CharField(**code_default)
	part_of_farm = CharField(**text_default)  # represent a named region in the farm
	spatial_data = CharField(**text_default)            
	land_use_restriction = ForeignKey('LandUse')            
	assessment = ForeignKey('Assessment')


class Assessment(Model):	
	soil_sample  = ForeignKey('SoilSample')
	analysis = ForeignKey('Analysis')
	status = ForeignKey('RecordedStatus')
        
		
class GenericStatus(Model):            
	staus = CharField(**code_default)
	status_name = CharField(**name_default)
	meaning = CharField(**text_default)
	
	
class RecordedStatus(Model):
	# Recorded Status @comment: references the present status of an entity
	status = ForeignKey('GenericStatus')
	status_date = DateField(**date_default)
	status_time = TimeField(**time_default)


class LandUse(Model):
	land_use = CharField(**text_default)  # CharField(**text_default) describing land use were land_use_code_type is insufficient
	land_use_type = CharField(**code_default)  # values: PRIMARY_CROP CATCH_CROP PRECEEDING_CROP LAND_USE_RESTRICTION
	farming_attribute = CharField(**code_default) # values: PLOUGHLESS DIRECT_SOWING
	land_use_restriction_type = CharField(**code_default)

		
class FertilizationRecommendation(Model):	 
	crops asbie
	agent asbie
	form_of_fertilizer asbie
	substance_contained CharField(**text_default)  # provide a list of content as delimieted string
	fertilizer asbie
	application_quantity DecimalField(**number_default)
	application_measured_unit CharField(**code_default)            

	
class SampleBase(Model):	
	recieved_date = DateField(**date_default)
	received_time = TimeField(**number_default)
	description = CharField(**text_default)
	comment = CharField(**text_default)
	weight = DecimalField(**number_default) 
	weight_unit = CharField(**code_default)
	volume = DecimalField(**number_default)
	volume_unit = CharField(**code_default)
	composition = CharField(**text_default)  # delimited string list
	information_source = CharField(**text_default)  # CharField(**name_default) of agency performing test
	source_certificate = CharField(**text_default)  # certification DecimalField(**number_default) or id for agency
	concentration = CharField(**text_default) # delimited string list of composed substance and their measurements
	analysis_date = DateField(**date_default)
	analysis_time = TimeField(**number_default)


class SoilSample(Model):	
	soil_name = CharField(**text_default)  # Give alternative CharField(**name_default) to soil type where not available in CharField(**code_default)
	soil_type = CharField(**code_default)
	reference_part_of_field = CharField(**text_default)
	spatial_data = CharField(**text_default)
	referenced_field = ForeignKey('FarmField')  # references the field segment on farm
	depth = DecimalField(**number_default)
	depth_unit = CharField(**code_default)
	depth_range = CharField(**text_default)
	analysis_method = CharField(**text_default)
	soil_heaviness = CharField(**text_default)
	soil_nutrient_classification = CharField(**text_default)
	soil_texture = CharField(**text_default)
        

class AnalysisResult(Model):            
	abstract_analysis = CharField(**text_default)
	parameters = CharField(**text_default)  # delimited string list. e.g {PH_VALUE: "method" "value" "classification" }
	description = CharField(**text_default)
	method = CharField(**text_default)
	comment = CharField(**text_default)
	sample = ForeignKey('ReportedSample')


class Fertilizer(Model):	
	fertilizer_brand = CharField(**text_default)  # general market brand CharField(**name_default)
	fertlizer_name = CharField(**text_default)  # specific manufacturer CharField(**name_default)
	fertilizer_type = CharField(**code_default)
	fertilizer_manufacturer = CharField(**text_default) for others
	supplier = ForeignKey('User')  # the agent supplying fertilizer
	fertilizer_form = CharField(**text_default)


class FieldCultivation(Model):         
	farm_field = ForeignKey('FarmField')
	reference_field_part = ForeignKey('FarmField')
	duration_of_use = DecimalField(**number_default)
	duration_unit = CharField(**code_default)                        

	
class Crop(Model):
	farm_field = ForeignKey('FarmField')
	monetary_value_per_hectar = DecimalField(**number_default)
	monetary_value_currency = CharField(**code_default)
	crop_growth_event = ForeignKey('CropGrowthStage')
	botanical_name = CharField(**name_default)
	cultural_name CharField(**name_default)
	description CharField(**text_default)
        
		
class CropGrowthStage(Model):            
	growth_stage = CharField(**text_default)
	date_recorded = DateField(**date_default)
	time_recorded = TimeField(**number_default)
	observer = CharField(**text_default)  # reference unique id of user that observed growth or name of agent/3rd party
	reported_by = ForeignKey('User')  # user reporting growth stage
            
class CropSpecies(Model):
	crop = ForeignKey('Crop')	
	name = CharField(**name_default)
	variety = CharField(**code_default)
	genetically_modified_organism = BooleanField(**bool_default)


class Harvest(Model):
	crop = ForeignKey('Crop')
	harvested_quantity = DecimalField(**number_default)
	yield_quantity = DecimalField(**number_default)
	quantity_unit = CharField(**code_default)
	# The name or string repr which can be parsed by target enum type.
	# The enum will have a default OTHER for cases not yet identified
	# Enum flag OTHER will enable collection and processing users CharField(**text_default) data
	harvest_quality = CharField(**code_default)
	farm_field = ForeignKey('FarmField')
	start_date = DateField(**date_default)
	end_date = DateField(**date_default)


class Activity(Model):
	daily_start = DateTimefield(**datetime_default)
	daily_end = DateTimefield(**datetime_default)
	activity = CharField(**text_default)
	comment = CharField(**text_default)
	work_done = CharField(**text_default)
	percentage_executed = DecimalField(**number_default)
	reference = GenericField()  # generic reference to Harvest Cultivation and other farming activities

class Weather(Model):
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
	reported_by = ForeignKey('User')
# can be weather station or 3rd party agent
	reported_date = DateField(**date_default)
	reported_time = TimeField(**number_default)
	measured_date = DateField(**date_default)
# use this field for weather condition measured by on farm
	measured_time = TimeField(**number_default)
	measured_by = ForeignKey('User')


class Contamination(Model):
	contaimination_type = CharField(**text_default)
	contamination_degree = CharField(**text_default)
	noticed_date = DateField(**date_default)
	noticed_time = TimeField(**number_default)
	reported_by = ForeignKey('User')
	affected_fields = ForeignKey('FarmField')
               
class AgriculturalProgramme 
	# @e.g palm seedling donations
	start = DateTimeField(**datetime_default)
	end = DateTimeField(**datetime_default)
	invitations = CharField(**text_default)
	consultants = CharField(**text_default)
	purpose = CharField(**text_default)
	description = CharField(**text_default)
	kpis = ForeignKey('MeasuredKPI')
	targets = CharField(**text_default)
	comments = CharField(**text_default)
	status = ForeignKey('RecordedStatus')

class ProgrammePerformance(Model):
	participants asbie  # reference a registered user or identifier for persons at event
# actual record of participants as against invitation            
	programme_activities = ForeignKey('Activity')  # reference the generic activity model
	comments = CharField(**text_default)
	learning_points = CharField(**text_default)
# learning from the event by organisers
	recommendations = CharField(**text_default)
# should hold organisers recommendations for later
	participant_suggestions = CharField(**text_default)
# should hold participants suggestions/recommendations
	event_coverage = BinaryField()  # uploaded photos or videos
	
	
class MeasuredKPI(Model):
	measured_kpis = CharField(**name_default)
# delimited CharField(**text_default) for the KPIs measured with their unit
	impact_assessment = CharField(**text_default)
	programme_performance = ForeignKey('ProgrammePerformance')

		
class FertilizerSample(SampleBase):
	fertilizer = ForeignKey('Fertilizer')	
