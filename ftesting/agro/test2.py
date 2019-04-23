#
#
#
class AgriculturalProgramme(models.Model):
		def __init__(self, [('start', 'datetime_'), ('end', 'datetime_'), ('invitations', 'asbie'), ('consultants', 'asbie'), ('purpose', 'text'), ('description', 'text'), ('kpis', 'asbie'), ('targets', 'text'), ('comments', 'text'), ('status', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.agriculturalProgrammeLock = threading.RLock()
			targets = models.TextField()
			end = models.D()
			description = models.TextField()
			start = models.D()
			purpose = models.TextField()
			comments = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class RecordedStatus(models.Model):
		def __init__(self, [('status', 'asbie'), ('status_date', 'date_'), ('status_time', 'time_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.recordedStatusLock = threading.RLock()
			status_time = models.T()
			status_date = models.D()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class SoilSample(models.Model):
		def __init__(self, [('soil_name', 'text'), ('soil_type', 'code'), ('reference_part_of_field', 'text'), ('spatial_data', 'text'), ('referenced_field', 'asbie'), ('depth', 'number'), ('depth_unit', 'code'), ('depth_range', 'text'), ('analysis_method', 'text'), ('soil_heaviness', 'text'), ('soil_nutrient_classification', 'text'), ('soil_texture', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.soilSampleLock = threading.RLock()
			soil_name = models.TextField()
			reference_part_of_field = models.TextField()
			spatial_data = models.TextField()
			soil_texture = models.TextField()
			depth_range = models.TextField()
			analysis_method = models.TextField()
			soil_type = models.I()
			soil_nutrient_classification = models.TextField()
			soil_heaviness = models.TextField()
			depth_unit = models.I()
			depth = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Crop(models.Model):
		def __init__(self, [('field', 'asbie'), ('monetary_value_per_hectar', 'number'), ('monetary_value_currency', 'code'), ('crop_growth_event', 'asbie'), ('botanical_name', 'name'), ('cultural_name', 'name'), ('description', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropLock = threading.RLock()
			cultural_name = models.CharField()
			description = models.TextField()
			monetary_value_per_hectar = models.I()
			botanical_name = models.CharField()
			monetary_value_currency = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Farm(models.Model):
		def __init__(self, [('fields', 'asbie'), ('name', 'text'), ('owner', 'asbie'), ('location', 'asbie'), ('description', 'text'), ('purpose', 'text'), ('certificate', 'asbie'), ('agric_programme', 'asbie'), ('size', 'asbie'), ('farming_system', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.farmLock = threading.RLock()
			name = models.TextField()
			farming_system = models.TextField()
			description = models.TextField()
			purpose = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class GenericStatus(models.Model):
		def __init__(self, [('staus', 'code'), ('status_name', 'name'), ('meaning', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.genericStatusLock = threading.RLock()
			staus = models.I()
			status_name = models.CharField()
			meaning = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Contamination(models.Model):
		def __init__(self, [('contaimination_type', 'text'), ('contamination_degree', 'text'), ('noticed_date', 'date_'), ('noticed_time', 'time_'), ('reported_by', 'asbie'), ('affected_fields', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.contaminationLock = threading.RLock()
			contaimination_type = models.TextField()
			noticed_date = models.D()
			contamination_degree = models.TextField()
			noticed_time = models.T()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Fertilizer(models.Model):
		def __init__(self, [('fertilizer_brand', 'text'), ('fertlizer_name', 'text'), ('fertilizer_type', 'code'), ('fertilizer_manufacturer', 'asbie'), ('supplier', 'asbie'), ('fertilizer_form', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizerLock = threading.RLock()
			fertilizer_form = models.TextField()
			fertilizer_brand = models.TextField()
			fertilizer_type = models.I()
			fertlizer_name = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class CropSpecies(models.Model):
		def __init__(self, [('crop', 'asbie'), ('name', 'text'), ('variety', 'code'), ('genetically_modified_organism', 'boolean')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropSpeciesLock = threading.RLock()
			genetically_modified_organism = models.B()
			name = models.TextField()
			variety = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class AnalysisResult(models.Model):
		def __init__(self, [('abstract_analysis', 'text'), ('parameters', 'text'), ('description', 'text'), ('method', 'text'), ('comment', 'text'), ('sample', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.analysisResultLock = threading.RLock()
			description = models.TextField()
			comment = models.TextField()
			parameters = models.TextField()
			abstract_analysis = models.TextField()
			method = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Certificate(models.Model):
		def __init__(self, [('first_certificate_date', 'date_'), ('certification_agency', 'text'), ('validity', 'asbie'), ('certificate_number', 'identifier'), ('certification_code', 'code'), ('supporting_documents', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.certificateLock = threading.RLock()
			first_certificate_date = models.D()
			certificate_number = models.I()
			certification_code = models.I()
			certification_agency = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Assessment(models.Model):
		def __init__(self, [('soil_sample', 'asbie'), ('analysis', 'asbie'), ('status', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.assessmentLock = threading.RLock()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class AgroDocument(models.Model):
		def __init__(self, [('contract_number', 'identifier'), ('farm', 'asbie'), ('work_process', 'asbie'), ('profile', 'text')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.agroDocumentLock = threading.RLock()
			profile = models.TextField()
			contract_number = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class FertilizationRecommendation(models.Model):
		def __init__(self, [('crops', 'asbie'), ('agent', 'asbie'), ('form_of_fertilizer', 'asbie'), ('substance_contained', 'text'), ('fertilizer', 'asbie'), ('application_quantity', 'number'), ('application_measured_unit', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizationRecommendationLock = threading.RLock()
			application_measured_unit = models.I()
			application_quantity = models.I()
			substance_contained = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class ProgrammePerformance(models.Model):
		def __init__(self, [('participants', 'text'), ('programme_activities', 'text'), ('comments', 'text'), ('learning_points', 'text'), ('recommendations', 'text'), ('participant_suggestions', 'text'), ('event_coverage', 'binary'), ('activity', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.programmePerformanceLock = threading.RLock()
			learning_points = models.TextField()
			participants = models.TextField()
			event_coverage = models.B()
			participant_suggestions = models.TextField()
			recommendations = models.TextField()
			programme_activities = models.TextField()
			comments = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class CertificationValidity(models.Model):
		def __init__(self, [('valid_for_purpose', 'boolean'), ('farm_purpose', 'text'), ('issue_date', 'date_'), ('start_date', 'date_'), ('expiry_date', 'date_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.certificationValidityLock = threading.RLock()
			start_date = models.D()
			farm_purpose = models.TextField()
			valid_for_purpose = models.B()
			expiry_date = models.D()
			issue_date = models.D()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class CropGrowthStage(models.Model):
		def __init__(self, [('growth_stage', 'text'), ('"date_"recorded', 'date_'), ('time_recorded', 'time_'), ('observer', 'text'), ('reported_by', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.cropGrowthStageLock = threading.RLock()
			observer = models.TextField()
			time_recorded = models.T()
			growth_stage = models.TextField()
			"date_"recorded = models.D()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Activity(models.Model):
		def __init__(self, [('daily_start', 'datetime_'), ('daily_end', 'datetime_'), ('activity', 'text'), ('comment', 'text'), ('work_done', 'text'), ('percentage_executed', 'number'), ('reference', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.activityLock = threading.RLock()
			comment = models.TextField()
			activity = models.TextField()
			daily_end = models.D()
			percentage_executed = models.I()
			daily_start = models.D()
			work_done = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class FieldCultivation(models.Model):
		def __init__(self, [('field', 'asbie'), ('reference_field_part', 'asbie'), ('duration_of_use', 'number'), ('duration_unit', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fieldCultivationLock = threading.RLock()
			duration_unit = models.I()
			duration_of_use = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Harvest(models.Model):
		def __init__(self, [('crop', 'asbie'), ('harvested_quantity', 'number'), ('yield_quantity', 'number'), ('quantity_unit', 'code'), ('harvest_quality', 'code'), ('field', 'asbie'), ('start_date', 'date_'), ('end_date', 'date_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.harvestLock = threading.RLock()
			start_date = models.D()
			yield_quantity = models.I()
			end_date = models.D()
			harvested_quantity = models.I()
			harvest_quality = models.I()
			quantity_unit = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class FarmField(models.Model):
		def __init__(self, [('cultivation', 'asbie'), ('name_of_field', 'name'), ('field_identification', 'identifier'), ('unique_area_id', 'identifier'), ('part_of_farm', 'text'), ('area', 'number'), ('area_unit', 'code'), ('spatial_data', 'asbie'), ('land_use_restriction', 'asbie'), ('assessment', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.farmFieldLock = threading.RLock()
			part_of_farm = models.TextField()
			area = models.I()
			field_identification = models.I()
			name_of_field = models.CharField()
			unique_area_id = models.I()
			area_unit = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class FertilizerSample(models.Model):
		def __init__(self, [('fertilizer', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.fertilizerSampleLock = threading.RLock()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class Weather(models.Model):
		def __init__(self, [('temperature', 'number'), ('temperature_unit', 'code'), ('wind_speed', 'number'), ('wind_speed_unit', 'code'), ('humidity', 'number'), ('humidity_unit', 'code'), ('precipitation', 'number'), ('precipitation_unit', 'code'), ('solar_radiation', 'number'), ('solar_radiation_unit', 'code'), ('reported_by', 'asbie'), ('reported_date', 'date_'), ('reported_time', 'time_'), ('measured_date', 'date_'), ('measured_time', 'time_'), ('measured_by', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.weatherLock = threading.RLock()
			humidity_unit = models.I()
			measured_time = models.T()
			reported_time = models.T()
			precipitation = models.I()
			measured_date = models.D()
			solar_radiation = models.I()
			wind_speed_unit = models.I()
			temperature_unit = models.I()
			solar_radiation_unit = models.I()
			wind_speed = models.I()
			precipitation_unit = models.I()
			temperature = models.I()
			humidity = models.I()
			reported_date = models.D()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class MeasuredKPI(models.Model):
		def __init__(self, [('measured_kpis', 'asbie'), ('impact_assessment', 'text'), ('programme_performance', 'asbie')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.measuredKPILock = threading.RLock()
			impact_assessment = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class LandUse(models.Model):
		def __init__(self, [('land_use', 'text'), ('land_use_type', 'code'), ('farming_attribute', 'code'), ('land_use_restriction_type', 'code')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.landUseLock = threading.RLock()
			land_use_restriction_type = models.I()
			farming_attribute = models.I()
			land_use = models.TextField()
			land_use_type = models.I()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

#
#
#
class SampleBase(models.Model):
		def __init__(self, [('recieved_date', 'date_'), ('received_time', 'time_'), ('description', 'text'), ('comment', 'text'), ('weight', 'number'), ('weight_unit', 'code'), ('volume', 'number'), ('volume_unit', 'code'), ('composition', 'text'), ('information_source', 'text'), ('source_certificate', 'text'), ('concentration', 'text'), ('analysis_date', 'date_'), ('analysis_time', 'time_')], **kwds):
			'''
				Comment this Method
			'''
			models.Model.__init__(self)
			try:
				self.sampleBaseLock = threading.RLock()
			analysis_time = models.T()
			received_time = models.T()
			source_certificate = models.TextField()
			composition = models.TextField()
			volume = models.I()
			concentration = models.TextField()
			weight = models.I()
			recieved_date = models.D()
			comment = models.TextField()
			analysis_date = models.D()
			weight_unit = models.I()
			volume_unit = models.I()
			information_source = models.TextField()
			description = models.TextField()

			except Exception, e:
				raise Exception(
					'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
				)

