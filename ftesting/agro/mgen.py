from  dbx2yaml import database

classes=[]

for table in database:
    y={};yaml={};yf={}
    for field in database[table]:
        #print("table=",table,"; field=",field[0])
        yf[field[0]]=field[1]
    y["Name"]=table
    y["Super"]='models.Model'
    y["DocString"]='You better comment this class'
    y["Args"]=database[table]
    y["Kwds"]=None
    y["Methods"]=None
    yaml['Class']=y
    classes.append(yaml)

from django_gen import get_dict
from django_gen import DjangoGen
for c in classes:
    options=get_dict(c)
    print (DjangoGen.generate(options))

