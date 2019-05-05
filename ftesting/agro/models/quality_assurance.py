

class FieldCultivation(BaseModel):	
	farm_field = ForeignKey('farming.FarmField')
	cultivation = ForeignKey(Cultivation)	
	duration_of_use = DurationField()
	duration_unit = CharField(**code_default) 
	crop = ManyToManyField(Crop)


class SampleBase(BaseModel):	
	recieved_datetime = DateTimeField(**date_default)	
	description = CharField(**text_default)
	comment = CharField(**text_default)
	weight = DecimalField(**number_default) 
	weight_unit = CharField(**code_default)
	volume = DecimalField(**number_default)
	volume_unit = CharField(**code_default)
	composition = TextField(**text_default)  # delimited string list
	information_source = CharField(**name_default)  # name or identifier of agency performing test or gathering sample 
	concentration = TextField(**text_default) # delimited string list of composed substance and their measurements	

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('quality_assurance:sample_base:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('quality_assurance:sample_base:update', args=(self.pk,))


class SoilSample(BaseModel):	
	soil_name = CharField(**text_default)  # Give alternative CharField(**name_default) to soil type where not available in CharField(**code_default)
	soil_type = CharField(**code_default)	
	spatial_data = TextField()  # identifies source of sample
	referenced_field = ForeignKey('FarmField')  # references the field segment on farm
	depth = DecimalField(**number_default)
	depth_unit = CharField(**code_default)
	depth_range = CharField(**text_default)	
	soil_heaviness = CharField(**text_default)
	soil_nutrient_classification = JSONField(**text_default)
	soil_texture = CharField(**text_default)
	analysis = ForeignKey('AnalysisResult')
        

class AnalysisResult(BaseModel):	
	analysis = TextField()  # delimited string list. e.g {PH_VALUE: "method" "value" "classification" }
	description = CharField(**text_default)
	method = CharField(**text_default)
	comment = CharField(**text_default)
	sample = ForeignKey('SoilSample')
	status = CharField()	
	analysis_datetime = DateTimeField(**date_default)	
	analysis_performed_by = CharField(**name_default)  # certification DecimalField(**number_default) or id for agency


class Fertilizer(BaseModel):	
	fertilizer_brand = CharField(**text_default)  # general market brand name
	fertlizer_name = CharField(**text_default)  # specific manufacturer name
	fertilizer_type = CharField(**code_default)
	fertilizer_manufacturer = CharField(**text_default) 
	supplier = CharField(**name_default)  # the agent supplying fertilizer or identifier
	fertilizer_form = CharField(**text_default)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizer_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_fertilizer_update', args=(self.pk,))

	
class FertilizationRecommendation(BaseModel):	
    application_measured_unit = CharField(**code_default)  # safer to use decimal and some quantities may be fractions
    application_quantity = DecimalField(**decimal_default)  # safer to use decimal and some quantities may be fractions
    substance_contained = TextField()
	farm_field = ForeignKey('FarmField', on_delete=models.DO_NOTHING)
	fertilizer = ForeignKey('Fertilizer', on_delete=models.DO_NOTHING, null=True)
	applicable_combinations = JSONField(null=True, editable=False) # Give the combination of Urea, SSP, MOP, CAN etc based on Nitrogen (N), Phosphorous (P), and Potassium (K) in soil sample

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_app_fertilizationrecommendation_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_app_fertilizationrecommendation_update', args=(self.pk,))