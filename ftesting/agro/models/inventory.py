

class Inventory(BaseModel):	
	reorder_level = IntegerField(default=0)
	reorder_quantity = IntegerField(default=0)
	details = TextField() # store detail information as json	
	object_id = PositiveIntegerField()
	asset = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('asset', 'object_id')	
		
class StockTaking(Event):	
	quantity = IntegerField()
	inventory = ForeignKey('inventory.Inventory')
	
class FarmProduce(BaseModel):	
	product_name = CharField(**name_default)
	cultural_name = CharField(**name_default)
    brand_name = CharField(**name_default)
    estimated_value = DecimalField(**decimal_default)
    market_value = DecimalField(**decimal_default)
    product_code = CharField(**code_default)

class CatalogueProduct(BaseModel):              
	object_id = PositiveIntegerField()
	source = ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	content_object = GenericForeignKey('source', 'object_id')
    product = ForeignKey(FarmProduce, on_delete=models.CASCADE, related_name='farm_produce')

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('inventory:catalogue_product:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('inventory:catalogue_product:update', args=(self.pk,))
