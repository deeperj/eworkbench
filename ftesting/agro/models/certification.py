

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
