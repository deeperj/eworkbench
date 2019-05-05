

class AgroDocument(BaseModel):	
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
	documents = ManyToManyField('AgroDocument')	
	signature_hash = CharField()
	signature_image = BinaryField()
	signature_timestamp = DateTimeField()


class GenericStatus(NamedCodes):    
	code = CharField(**name_default)
	name = CharField(**name_default)
	description = TextField()
	
	def save(self, *args, **kwargs):
		# ensure only codes from the status enum are saved
		pass

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('util:generic_status:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('util:generic_status:update', args=(self.pk,))		


class RecordedStatus(BaseModel):	
	status = ForeignKey('GenericStatus')
    recorded_datetime = DateTimeField()	    	
	object_id = PositiveIntergerField()
	content_type = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('util:recorded_status:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('util:recorded_status:update', args=(self.pk,))