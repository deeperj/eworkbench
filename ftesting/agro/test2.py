#
#
#
class FertilizationRecommendation(models.Model):
	application_measured_unit = models.IntegerField()
	application_quantity = models.IntegerField()
	substance_contained = models.TextField()

#
#
#
class AgroDocument(models.Model):
	contract_number = models.IntegerField()
	profile = models.TextField()

#
#
#
class Activity(models.Model):
	daily_start = models.DateTimeField()
	activity = models.TextField()
	comment = models.TextField()
	percentage_executed = models.IntegerField()
	daily_end = models.DateTimeField()
	work_done = models.TextField()

#
#
#
class AgriculturalProgramme(models.Model):
	comments = models.TextField()
	end = models.DateTimeField()
	targets = models.TextField()
	description = models.TextField()
	start = models.DateTimeField()
	purpose = models.TextField()

#
#
#
class Certificate(models.Model):
	first_certificate_date = models.DateField()
	certification_code = models.IntegerField()
	certificate_number = models.IntegerField()
	certification_agency = models.TextField()

#
#
#
class Crop(models.Model):
	cultural_name = models.CharField()
	monetary_value_per_hectar = models.IntegerField()
	description = models.TextField()
	monetary_value_currency = models.IntegerField()
	botanical_name = models.CharField()

#
#
#
class FieldCultivation(models.Model):
	duration_unit = models.IntegerField()
	duration_of_use = models.IntegerField()

#
#
#
class Weather(models.Model):
	precipitation_unit = models.IntegerField()
	humidity_unit = models.IntegerField()
	humidity = models.IntegerField()
	wind_speed = models.IntegerField()
	temperature = models.IntegerField()
	temperature_unit = models.IntegerField()
	reported_date = models.DateField()
	measured_date = models.DateField()
	solar_radiation_unit = models.IntegerField()
	wind_speed_unit = models.IntegerField()
	measured_time = models.TimeField()
	solar_radiation = models.IntegerField()
	precipitation = models.IntegerField()
	reported_time = models.TimeField()

#
#
#
class SampleBase(models.Model):
	source_certificate = models.TextField()
	received_time = models.TimeField()
	concentration = models.TextField()
	weight_unit = models.IntegerField()
	recieved_date = models.DateField()
	volume = models.IntegerField()
	analysis_date = models.DateField()
	comment = models.TextField()
	description = models.TextField()
	information_source = models.TextField()
	volume_unit = models.IntegerField()
	analysis_time = models.TimeField()
	weight = models.IntegerField()
	composition = models.TextField()

#
#
#
class CertificationValidity(models.Model):
	issue_date = models.DateField()
	start_date = models.DateField()
	farm_purpose = models.TextField()
	expiry_date = models.DateField()
	valid_for_purpose = models.BooleanField()

#
#
#
class SoilSample(models.Model):
	soil_texture = models.TextField()
	analysis_method = models.TextField()
	soil_heaviness = models.TextField()
	soil_name = models.TextField()
	spatial_data = models.TextField()
	reference_part_of_field = models.TextField()
	soil_nutrient_classification = models.TextField()
	depth_range = models.TextField()
	soil_type = models.IntegerField()
	depth_unit = models.IntegerField()
	depth = models.IntegerField()

#
#
#
class RecordedStatus(models.Model):
	status_date = models.DateField()
	status_time = models.TimeField()

#
#
#
class Harvest(models.Model):
	quantity_unit = models.IntegerField()
	harvested_quantity = models.IntegerField()
	harvest_quality = models.IntegerField()
	end_date = models.DateField()
	yield_quantity = models.IntegerField()
	start_date = models.DateField()


#
#
#
class AnalysisResult(models.Model):
	parameters = models.TextField()
	method = models.TextField()
	comment = models.TextField()
	description = models.TextField()
	abstract_analysis = models.TextField()

#
#
#
class ProgrammePerformance(models.Model):
	event_coverage = models.BinaryField()
	programme_activities = models.TextField()
	comments = models.TextField()
	participants = models.TextField()
	learning_points = models.TextField()
	participant_suggestions = models.TextField()
	recommendations = models.TextField()

#
#
#
class Fertilizer(models.Model):
	fertilizer_type = models.IntegerField()
	fertlizer_name = models.TextField()
	fertilizer_brand = models.TextField()
	fertilizer_form = models.TextField()

#
#
#
class Farm(models.Model):
	purpose = models.TextField()
	description = models.TextField()
	name = models.TextField()
	farming_system = models.TextField()

#
#
#
class FarmField(models.Model):
	area = models.IntegerField()
	field_identification = models.IntegerField()
	area_unit = models.IntegerField()
	unique_area_id = models.IntegerField()
	name_of_field = models.CharField()
	part_of_farm = models.TextField()

#
#
#
class GenericStatus(models.Model):
	status_name = models.CharField()
	meaning = models.TextField()
	staus = models.IntegerField()

#
#
#
class CropGrowthStage(models.Model):
	time_recorded = models.TimeField()
	growth_stage = models.TextField()
	date_recorded = models.DateField()
	observer = models.TextField()


#
#
#
class CropSpecies(models.Model):
	genetically_modified_organism = models.BooleanField()
	variety = models.IntegerField()
	name = models.TextField()

#
#
#
class MeasuredKPI(models.Model):
	impact_assessment = models.TextField()

#
#
#
class LandUse(models.Model):
	land_use_type = models.IntegerField()
	farming_attribute = models.IntegerField()
	land_use_restriction_type = models.IntegerField()
	land_use = models.TextField()

#
#
#
class Contamination(models.Model):
	contamination_degree = models.TextField()
	noticed_date = models.DateField()
	contaimination_type = models.TextField()
	noticed_time = models.TimeField()

