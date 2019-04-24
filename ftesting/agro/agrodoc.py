
char_default = {
	length: 100,
}

date_default = {
	auto_now: False, 
	auto_now_add: False, 
	options: {}
}

datetime_default = {

}

code_default = {
	
}

bool_default = {

}

name_default = {

}

text_default = {

}

options = {
	: ,
}

#1
class AgroDocument(Model):	
	contract_number = models.UUIDField
	farm = models.ForeignKey(Farm)
	work_process = models.ForeignKey(WokProcess)            
	profile = models.CharField(**default_char)
	
