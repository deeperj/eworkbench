Class
#
#
#
class AgroDocument(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('contract_number', 'identifier'), ('farm', 'asbie'), ('work_process', 'asbie'), ('profile', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.agroDocumentLock = threading.RLock()
				self.contract_number = contract_number
				self.farm = farm
				self.work_process = work_process
				self.profile = profile

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Farm(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('fields', 'asbie'), ('name', 'text'), ('owner', 'asbie'), ('location', 'asbie'), ('description', 'text'), ('purpose', 'text'), ('certificate', 'asbie'), ('agric_programme', 'asbie'), ('size', 'asbie'), ('farming_system', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.farmLock = threading.RLock()
				self.fields = fields
				self.name = name
				self.owner = owner
				self.location = location
				self.description = description
				self.purpose = purpose
				self.certificate = certificate
				self.agric_programme = agric_programme
				self.size = size
				self.farming_system = farming_system

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Certificate(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('first_certificate_date', 'date_'), ('certification_agency', 'text'), ('validity', 'asbie'), ('certificate_number', 'identifier'), ('certification_code', 'code'), ('supporting_documents', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.certificateLock = threading.RLock()
				self.first_certificate_date = first_certificate_date
				self.certification_agency = certification_agency
				self.validity = validity
				self.certificate_number = certificate_number
				self.certification_code = certification_code
				self.supporting_documents = supporting_documents

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class CertificationValidity(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('valid_for_purpose', 'boolean'), ('farm_purpose', 'text'), ('issue_date', 'date_'), ('start_date', 'date_'), ('expiry_date', 'date_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.certificationValidityLock = threading.RLock()
				self.valid_for_purpose = valid_for_purpose
				self.farm_purpose = farm_purpose
				self.issue_date = issue_date
				self.start_date = start_date
				self.expiry_date = expiry_date

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class FarmField(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('cultivation', 'asbie'), ('name_of_field', 'name'), ('field_identification', 'identifier'), ('unique_area_id', 'identifier'), ('part_of_farm', 'text'), ('area', 'number'), ('area_unit', 'code'), ('spatial_data', 'asbie'), ('land_use_restriction', 'asbie'), ('assessment', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.farmFieldLock = threading.RLock()
				self.cultivation = cultivation
				self.name_of_field = name_of_field
				self.field_identification = field_identification
				self.unique_area_id = unique_area_id
				self.part_of_farm = part_of_farm
				self.area = area
				self.area_unit = area_unit
				self.spatial_data = spatial_data
				self.land_use_restriction = land_use_restriction
				self.assessment = assessment

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Assessment(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('soil_sample', 'asbie'), ('analysis', 'asbie'), ('status', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.assessmentLock = threading.RLock()
				self.soil_sample = soil_sample
				self.analysis = analysis
				self.status = status

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class GenericStatus(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('staus', 'code'), ('status_name', 'name'), ('meaning', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.genericStatusLock = threading.RLock()
				self.staus = staus
				self.status_name = status_name
				self.meaning = meaning

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class RecordedStatus(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('status', 'asbie'), ('status_date', 'date_'), ('status_time', 'time_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.recordedStatusLock = threading.RLock()
				self.status = status
				self.status_date = status_date
				self.status_time = status_time

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class LandUse(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('land_use', 'text'), ('land_use_type', 'code'), ('farming_attribute', 'code'), ('land_use_restriction_type', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.landUseLock = threading.RLock()
				self.land_use = land_use
				self.land_use_type = land_use_type
				self.farming_attribute = farming_attribute
				self.land_use_restriction_type = land_use_restriction_type

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class FertilizationRecommendation(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('crops', 'asbie'), ('agent', 'asbie'), ('form_of_fertilizer', 'asbie'), ('substance_contained', 'text'), ('fertilizer', 'asbie'), ('application_quantity', 'number'), ('application_measured_unit', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizationRecommendationLock = threading.RLock()
				self.crops = crops
				self.agent = agent
				self.form_of_fertilizer = form_of_fertilizer
				self.substance_contained = substance_contained
				self.fertilizer = fertilizer
				self.application_quantity = application_quantity
				self.application_measured_unit = application_measured_unit

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class SampleBase(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('recieved_date', 'date_'), ('received_time', 'time_'), ('description', 'text'), ('comment', 'text'), ('weight', 'number'), ('weight_unit', 'code'), ('volume', 'number'), ('volume_unit', 'code'), ('composition', 'text'), ('information_source', 'text'), ('source_certificate', 'text'), ('concentration', 'text'), ('analysis_date', 'date_'), ('analysis_time', 'time_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.sampleBaseLock = threading.RLock()
				self.recieved_date = recieved_date
				self.received_time = received_time
				self.description = description
				self.comment = comment
				self.weight = weight
				self.weight_unit = weight_unit
				self.volume = volume
				self.volume_unit = volume_unit
				self.composition = composition
				self.information_source = information_source
				self.source_certificate = source_certificate
				self.concentration = concentration
				self.analysis_date = analysis_date
				self.analysis_time = analysis_time

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class SoilSample(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('soil_name', 'text'), ('soil_type', 'code'), ('reference_part_of_field', 'text'), ('spatial_data', 'text'), ('referenced_field', 'asbie'), ('depth', 'number'), ('depth_unit', 'code'), ('depth_range', 'text'), ('analysis_method', 'text'), ('soil_heaviness', 'text'), ('soil_nutrient_classification', 'text'), ('soil_texture', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.soilSampleLock = threading.RLock()
				self.soil_name = soil_name
				self.soil_type = soil_type
				self.reference_part_of_field = reference_part_of_field
				self.spatial_data = spatial_data
				self.referenced_field = referenced_field
				self.depth = depth
				self.depth_unit = depth_unit
				self.depth_range = depth_range
				self.analysis_method = analysis_method
				self.soil_heaviness = soil_heaviness
				self.soil_nutrient_classification = soil_nutrient_classification
				self.soil_texture = soil_texture

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class AnalysisResult(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('abstract_analysis', 'text'), ('parameters', 'text'), ('description', 'text'), ('method', 'text'), ('comment', 'text'), ('sample', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.analysisResultLock = threading.RLock()
				self.abstract_analysis = abstract_analysis
				self.parameters = parameters
				self.description = description
				self.method = method
				self.comment = comment
				self.sample = sample

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class FertilizerSample(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('fertilizer', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizerSampleLock = threading.RLock()
				self.fertilizer = fertilizer

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Fertilizer(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('fertilizer_brand', 'text'), ('fertlizer_name', 'text'), ('fertilizer_type', 'code'), ('fertilizer_manufacturer', 'asbie'), ('supplier', 'asbie'), ('fertilizer_form', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizerLock = threading.RLock()
				self.fertilizer_brand = fertilizer_brand
				self.fertlizer_name = fertlizer_name
				self.fertilizer_type = fertilizer_type
				self.fertilizer_manufacturer = fertilizer_manufacturer
				self.supplier = supplier
				self.fertilizer_form = fertilizer_form

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class FieldCultivation(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('field', 'asbie'), ('reference_field_part', 'asbie'), ('duration_of_use', 'number'), ('duration_unit', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fieldCultivationLock = threading.RLock()
				self.field = field
				self.reference_field_part = reference_field_part
				self.duration_of_use = duration_of_use
				self.duration_unit = duration_unit

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Crop(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('field', 'asbie'), ('monetary_value_per_hectar', 'number'), ('monetary_value_currency', 'code'), ('crop_growth_event', 'asbie'), ('botanical_name', 'name'), ('cultural_name', 'name'), ('description', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropLock = threading.RLock()
				self.field = field
				self.monetary_value_per_hectar = monetary_value_per_hectar
				self.monetary_value_currency = monetary_value_currency
				self.crop_growth_event = crop_growth_event
				self.botanical_name = botanical_name
				self.cultural_name = cultural_name
				self.description = description

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class CropGrowthStage(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('growth_stage', 'text'), ('"date_"recorded', 'date_'), ('time_recorded', 'time_'), ('observer', 'text'), ('reported_by', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropGrowthStageLock = threading.RLock()
				self.growth_stage = growth_stage
				self."date_"recorded = "date_"recorded
				self.time_recorded = time_recorded
				self.observer = observer
				self.reported_by = reported_by

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class CropSpecies(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('crop', 'asbie'), ('name', 'text'), ('variety', 'code'), ('genetically_modified_organism', 'boolean')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropSpeciesLock = threading.RLock()
				self.crop = crop
				self.name = name
				self.variety = variety
				self.genetically_modified_organism = genetically_modified_organism

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Harvest(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('crop', 'asbie'), ('harvested_quantity', 'number'), ('yield_quantity', 'number'), ('quantity_unit', 'code'), ('harvest_quality', 'code'), ('field', 'asbie'), ('start_date', 'date_'), ('end_date', 'date_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.harvestLock = threading.RLock()
				self.crop = crop
				self.harvested_quantity = harvested_quantity
				self.yield_quantity = yield_quantity
				self.quantity_unit = quantity_unit
				self.harvest_quality = harvest_quality
				self.field = field
				self.start_date = start_date
				self.end_date = end_date

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Activity(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('daily_start', 'datetime_'), ('daily_end', 'datetime_'), ('activity', 'text'), ('comment', 'text'), ('work_done', 'text'), ('percentage_executed', 'number'), ('reference', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.activityLock = threading.RLock()
				self.daily_start = daily_start
				self.daily_end = daily_end
				self.activity = activity
				self.comment = comment
				self.work_done = work_done
				self.percentage_executed = percentage_executed
				self.reference = reference

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Weather(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('temperature', 'number'), ('temperature_unit', 'code'), ('wind_speed', 'number'), ('wind_speed_unit', 'code'), ('humidity', 'number'), ('humidity_unit', 'code'), ('precipitation', 'number'), ('precipitation_unit', 'code'), ('solar_radiation', 'number'), ('solar_radiation_unit', 'code'), ('reported_by', 'asbie'), ('reported_date', 'date_'), ('reported_time', 'time_'), ('measured_date', 'date_'), ('measured_time', 'time_'), ('measured_by', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.weatherLock = threading.RLock()
				self.temperature = temperature
				self.temperature_unit = temperature_unit
				self.wind_speed = wind_speed
				self.wind_speed_unit = wind_speed_unit
				self.humidity = humidity
				self.humidity_unit = humidity_unit
				self.precipitation = precipitation
				self.precipitation_unit = precipitation_unit
				self.solar_radiation = solar_radiation
				self.solar_radiation_unit = solar_radiation_unit
				self.reported_by = reported_by
				self.reported_date = reported_date
				self.reported_time = reported_time
				self.measured_date = measured_date
				self.measured_time = measured_time
				self.measured_by = measured_by

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class Contamination(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('contaimination_type', 'text'), ('contamination_degree', 'text'), ('noticed_date', 'date_'), ('noticed_time', 'time_'), ('reported_by', 'asbie'), ('affected_fields', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.contaminationLock = threading.RLock()
				self.contaimination_type = contaimination_type
				self.contamination_degree = contamination_degree
				self.noticed_date = noticed_date
				self.noticed_time = noticed_time
				self.reported_by = reported_by
				self.affected_fields = affected_fields

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class AgriculturalProgramme(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('start', 'datetime_'), ('end', 'datetime_'), ('invitations', 'asbie'), ('consultants', 'asbie'), ('purpose', 'text'), ('description', 'text'), ('kpis', 'asbie'), ('targets', 'text'), ('comments', 'text'), ('status', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.agriculturalProgrammeLock = threading.RLock()
				self.start = start
				self.end = end
				self.invitations = invitations
				self.consultants = consultants
				self.purpose = purpose
				self.description = description
				self.kpis = kpis
				self.targets = targets
				self.comments = comments
				self.status = status

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class ProgrammePerformance(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('participants', 'text'), ('programme_activities', 'text'), ('comments', 'text'), ('learning_points', 'text'), ('recommendations', 'text'), ('participant_suggestions', 'text'), ('event_coverage', 'binary'), ('activity', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.programmePerformanceLock = threading.RLock()
				self.participants = participants
				self.programme_activities = programme_activities
				self.comments = comments
				self.learning_points = learning_points
				self.recommendations = recommendations
				self.participant_suggestions = participant_suggestions
				self.event_coverage = event_coverage
				self.activity = activity

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

Class
#
#
#
class MeasuredKPI(models.Model):
	'''
		You better comment this class
	'''
		def __init__(self, [('measured_kpis', 'asbie'), ('impact_assessment', 'text'), ('programme_performance', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.measuredKPILock = threading.RLock()
				self.measured_kpis = measured_kpis
				self.impact_assessment = impact_assessment
				self.programme_performance = programme_performance

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

