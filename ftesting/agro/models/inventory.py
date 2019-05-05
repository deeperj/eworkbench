
class Inventory(BaseModel):
	# Done
	reorder_level = IntegerField(default=0)
	reorder_quantity = IntegerField(default=0)
	details = JSONField()	
	object_id = PositiveIntegerField()
	asset = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('asset', 'object_id')	
		
class StockTaking(Event):
	# Done
	quantity = IntegerField
	inventory = ForeignKey(Inventory)
	
class FarmProduce(BaseModel):
	# Done
	product_name = CharField(**name_default)
	cultural_name = CharField(**name_default)
    brand_name = CharField(**name_default)
    estimated_value = DecimalField(**decimal_default)
    market_value = DecimalField(**decimal_default)
    product_code = CharField(**code_default)

class CatalogueProduct(BaseModel):
    # Done           
	object_id = PositiveIntegerField()
	source = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('source', 'object_id')
    product = ForeignKey(FarmProduce, on_delete=models.CASCADE, related_name='farm_produce')

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agro_farm_monitoring_animalproduct_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agro_farm_monitoring_animalproduct_update', args=(self.pk,))
