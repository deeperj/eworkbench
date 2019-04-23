'''
1. asbie: represents a relationship or complex data structure. E.g a dictionary object or foreign field in a table
2. name: repr alphanumeric string type of limited length. Default length set to 50 characters
3. text: repr raw string type. Default length set to 200 characters
4. code: repr alpanumeric string used to name a constant or flag. e.g PH_VALUE, COLOR_RED
5. number: repr numeric type either as a number or string that can be parsed into a number type
6. "date_": repr the date object
7. datetime_: repr the datetime object
8. time_: repr time object
9. "identifier": repr a unique identification for an attribute e.g a primary key for a table, a unique number, or index
10. amount: repr monetary values with their associated currency code
11. boolean: repr bool True or False values
12. binary: repr raw bytes or byte array like streams or object
from django.db.models import BinaryField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import TextField

'''
def asbie(empty):#1
    return None

def name(empty):#2
    return ("CharField","max_length=255")

def code(empty):#3
    return ("IntegerField",)

def number(empty):#4
    return ("IntegerField",)

def date_(empty):#5
    return ("DateField",)

def datetime_(empty):#6
    return ("DateTimeField",)

def time_(empty):#7
    return ("TimeField",)

def identifier(empty):#8
    return ("IntegerField",)

def amount(empty):#9
    return ("DecimalField",)

def text(empty):#10
    return ("TextField","max_length=255")

def boolean(empty):#11
    return ("BooleanField",)

def binary(empty):#12
    return ("BinaryField",)

def default(arg):#12
    return (arg,)

def dsel(argument):
    switcher = {
        "asbie": asbie, #1
        "name": name, #2
        "code": code, #3
        "number": number, #4
        "date_": date_, #5
        "datetime_": datetime_, #6
        "time_": time_, #7
        "identifier": identifier, #8
        "amount": amount, #9
        "text": text, #10
        "boolean": boolean, #11
        "binary": binary, #12
        "default": default, #12
        #"name": lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, switcher.get("default", lambda: "nothing"))
    # Execute the function
    return func(argument)