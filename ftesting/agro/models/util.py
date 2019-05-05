

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


class Signatures(models.Model):
    # Done
	documents = ManyToManyField('farm_monitoring.AgroDocument')	
	signature_hash = CharField()
	signature_image = BinaryField()
	signature_timestamp = DateTimeField()


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
