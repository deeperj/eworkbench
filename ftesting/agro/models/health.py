

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
