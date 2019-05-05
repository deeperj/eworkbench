from django.contrib.contentype.models import ContentType
from django.db import models
from django.db.models import CharField, BinaryField, DateField, \
    DateTimeField, TimeField, TextField, ForeignKey, UUIDField, BooleanField,\
    DecimalField, IntegerField, EmailField, FileField, ImageField
from agro_enterprise.settings import MEDIA_PATH

# @todo: add the various user types to enable easy referencing of users
# Farm models

binary_default = {
    'editable': False,
    'max_length': 500
}

char_default = {
    'max_length': 100,
}

date_default = {
    'auto_now': False,
    'auto_now_add': True,
}

datetime_default = date_default

decimal_default = {
    'max_digits': 20,
    'decimal_places': 2,
    'default': 0.00
}

file_default = {
    'upload_to': MEDIA_PATH,
    'max_length': 100
}

code_default = {
    'max_length': 15
}

bool_default = {
    'default': False
}

image_default = {
    'height_field': 150,
    'width_field': 150,
}

name_default = {
    'max_length': 100
}

time_default = date_default

text_default = {
    'max_length': 250
}

options = {
    'null': False,
    'blank': False,
    'choices': None,
    'default': None,
    'editable': False,
    'error_messages': None,
    'help_text': '',
    'primary_key': False,
    'unique': False,
    'unique_for_date': '',
    'unique_for_month': '',
    'unique_for_year':  '',
    'verbose_name': '',
    'validators': None,
}


class BaseModel(models.Model):
	# Done
	created_at = DateTimeField(auto_now_add=True)
	last_modified_at = DateField(auto_now=True)
	deleted_at = DateTimeField(auto_now_add=False, auto_now=False)
	enable_soft_delete = BooleanField(default=True)
	force_delete = BooleanField(default=False)

	def save(self, *args, **kwargs):
		# apply the soft delete concept on save
		pass
		
	def delete(self, *args, **kwargs):
		# apply the soft delete concept on delete
		# if force_delete = True, then delete from db irrespective of settings
		pass

	class Meta:
		abstract = True
			
		
class NamedCode(models.Model):
	# Done
	# The name or string repr which can be parsed by target enum type.
	# The enum will have a default OTHER for cases not yet identified
	# Enum flag OTHER will enable collection and processing 
	name = CharField(**name_default)
	code_value = CharField(**text_default)
	meaning = TextField()
	
	def parse_to_enum(self, name, value=None, enum_type=None):
		# return a given enum member for the given (name, value) pair in model record
		pass
		
	def parse_from_enum(self, enum_type=None, enum_value=None, enum_name=None):
		pass
	



