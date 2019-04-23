#
#
#
class MeasuredKPI(models.Model):
			impact_assessment = models.TextField()

#
#
#
class Harvest(models.Model):
			harvested_quantity = models.I()
			harvest_quality = models.I()
			yield_quantity = models.I()
			end_date = models.D()
			start_date = models.D()
			quantity_unit = models.I()

#
#
#
class CertificationValidity(models.Model):
			start_date = models.D()
			valid_for_purpose = models.B()
			expiry_date = models.D()
			issue_date = models.D()
			farm_purpose = models.TextField()

#
#
#
class SoilSample(models.Model):
			soil_name = models.TextField()
			analysis_method = models.TextField()
			reference_part_of_field = models.TextField()
			soil_heaviness = models.TextField()
			soil_type = models.I()
			depth_range = models.TextField()
			spatial_data = models.TextField()
			depth_unit = models.I()
			soil_nutrient_classification = models.TextField()
			soil_texture = models.TextField()
			depth = models.I()

#
#
#
class CropGrowthStage(models.Model):
			"date_"recorded = models.D()
			observer = models.TextField()
			time_recorded = models.T()
			growth_stage = models.TextField()

#
#
#
class Contamination(models.Model):
			contamination_degree = models.TextField()
			noticed_time = models.T()
			contaimination_type = models.TextField()
			noticed_date = models.D()

#
#
#
class FarmField(models.Model):
			unique_area_id = models.I()
			name_of_field = models.CharField()
			area = models.I()
			part_of_farm = models.TextField()
			area_unit = models.I()
			field_identification = models.I()

#
#
#
class Farm(models.Model):
			description = models.TextField()
			name = models.TextField()
			farming_system = models.TextField()
			purpose = models.TextField()

#
#
#
class FieldCultivation(models.Model):
			duration_unit = models.I()
			duration_of_use = models.I()

#
#
#
class FertilizerSample(models.Model):

#
#
#
class Assessment(models.Model):

#
#
#
class Fertilizer(models.Model):
			fertilizer_form = models.TextField()
			fertilizer_type = models.I()
			fertlizer_name = models.TextField()
			fertilizer_brand = models.TextField()

#
#
#
class Certificate(models.Model):
			first_certificate_date = models.D()
			certification_agency = models.TextField()
			certificate_number = models.I()
			certification_code = models.I()

#
#
#
class FertilizationRecommendation(models.Model):
			application_quantity = models.I()
			substance_contained = models.TextField()
			application_measured_unit = models.I()

#
#
#
class Weather(models.Model):
			humidity_unit = models.I()
			solar_radiation_unit = models.I()
			humidity = models.I()
			temperature_unit = models.I()
			precipitation_unit = models.I()
			measured_time = models.T()
			precipitation = models.I()
			wind_speed = models.I()
			solar_radiation = models.I()
			temperature = models.I()
			measured_date = models.D()
			wind_speed_unit = models.I()
			reported_date = models.D()
			reported_time = models.T()

#
#
#
class RecordedStatus(models.Model):
			status_time = models.T()
			status_date = models.D()

#
#
#
class LandUse(models.Model):
			land_use_restriction_type = models.I()
			land_use = models.TextField()
			farming_attribute = models.I()
			land_use_type = models.I()

#
#
#
class Crop(models.Model):
			description = models.TextField()
			cultural_name = models.CharField()
			botanical_name = models.CharField()
			monetary_value_currency = models.I()
			monetary_value_per_hectar = models.I()

#
#
#
class Activity(models.Model):
			percentage_executed = models.I()
			work_done = models.TextField()
			activity = models.TextField()
			comment = models.TextField()
			daily_end = models.D()
			daily_start = models.D()

#
#
#
class CropSpecies(models.Model):
			genetically_modified_organism = models.B()
			name = models.TextField()
			variety = models.I()

#
#
#
class AgriculturalProgramme(models.Model):
			purpose = models.TextField()
			description = models.TextField()
			targets = models.TextField()
			start = models.D()
			end = models.D()
			comments = models.TextField()

#
#
#
class ProgrammePerformance(models.Model):
			learning_points = models.TextField()
			recommendations = models.TextField()
			programme_activities = models.TextField()
			event_coverage = models.B()
			participant_suggestions = models.TextField()
			comments = models.TextField()
			participants = models.TextField()

#
#
#
class SampleBase(models.Model):
			information_source = models.TextField()
			source_certificate = models.TextField()
			comment = models.TextField()
			description = models.TextField()
			received_time = models.T()
			weight = models.I()
			analysis_date = models.D()
			recieved_date = models.D()
			weight_unit = models.I()
			concentration = models.TextField()
			volume_unit = models.I()
			analysis_time = models.T()
			composition = models.TextField()
			volume = models.I()

#
#
#
class GenericStatus(models.Model):
			staus = models.I()
			meaning = models.TextField()
			status_name = models.CharField()

#
#
#
class AgroDocument(models.Model):
			profile = models.TextField()
			contract_number = models.I()

#
#
#
class AnalysisResult(models.Model):
			description = models.TextField()
			abstract_analysis = models.TextField()
			comment = models.TextField()
			method = models.TextField()
			parameters = models.TextField()

