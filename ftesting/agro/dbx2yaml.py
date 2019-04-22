# Python definition of database structure

# Define the various database tables as list in the iterator
'''
The datatypes defined here do not comply with the native python object or framework model types
Efforts have been added to ensure names of datatypes are descriptive
It is believed that the average database designer will be able to decipher what datatype
to use for his/her target database or framework model. Below is a brief type description:
DATATYPES
=========
asbie: represents a relationship or complex data structure. E.g a dictionary object or foreign field in a table
name: repr alphanumeric string type of limited length. Default length set to 50 characters
text: repr raw string type. Default length set to 200 characters
code: repr alpanumeric string used to name a constant or flag. e.g PH_VALUE, COLOR_RED
number: repr numeric type either as a number or string that can be parsed into a number type
"date_": repr the date object
datetime_: repr the datetime object
time_: repr time object
"identifier": repr a unique identification for an attribute e.g a primary key for a table, a unique number, or index
amount: repr monetary values with their associated currency code
boolean: repr bool True or False values
binary: repr raw bytes or byte array like streams or object

'''

database = {
        "AgroDocument":[
            # 1. Agro Document extends the base UBL document model
            ('contract_number', "identifier"),            
            ('farm', "asbie"),            
            ('work_process', "asbie"),            
            ('profile', "text"),            
        ],
        "Farm":[
            # 2. Farm
            ('fields', "asbie"),  # references the various arable regions on the farm
            ('name', "text"),
            ('owner', "asbie"),
            ('location', "asbie"),  # use address type or GPS reading here
            ('description', "text"),
            ('purpose', "text"),
            ('certificate', "asbie"),
            ('agric_programme', "asbie"),
            ('size', "asbie"),  # gives the calculated land mass for the farm. Not necessarily sum of field area
            ('farming_system', "text")
        ],
        "Certificate":[
            # 3. Certificate
            ('first_certificate_date', "date_"),
            ('certification_agency', "text"),
            ('validity', "asbie"),
            ('certificate_number', "identifier"),
            ('certification_code', "code"),
            ('supporting_documents', "asbie"), # scanned paper documents where applicable
        ],
        "CertificationValidity":[
            # 4. Certification Validity
            ('valid_for_purpose', "boolean"),
            ('farm_purpose', "text"),
            ('issue_date', "date_"),
            ('start_date', "date_"), # defaults to issue_date when not specified
            ('expiry_date', "date_"),            
        ],
        "FarmField":[
            # 5. Field
            ('cultivation', "asbie"),            
            ('name_of_field', "name"),
            ('field_identification', "identifier"),
            ('unique_area_id', "identifier"),
            ('part_of_farm', 'text'),
            ('area', "number"),
            ('area_unit', "code"),
            ('spatial_data', "asbie"),
            ('land_use_restriction', "asbie"),
            ('assessment', "asbie"),
 # reference the soil_sample & analysis result            
        ],
        "Assessment":[
            # 6. Assessment
            ('soil_sample', "asbie"),
            ('analysis', "asbie"),
            ('status', "asbie")
        ],
        "GenericStatus":[
            # 7. Generic Status
            ('staus', "code"),
            ('status_name', "name"),
            ('meaning', "text")
        ],
        "RecordedStatus":[
            # 8. Recorded Status @comment: references the present status of an entity
            ('status', "asbie"),
            ('status_date', "date_"),
            ('status_time', "time_")
        ],
        "LandUse":[
            # 9. Land use
            ('land_use', "text"),  # text describing land use were land_use_code_type is insufficient
            ('land_use_type', "code"),  # values: PRIMARY_CROP, CATCH_CROP, PRECEEDING_CROP, LAND_USE_RESTRICTION
            ('farming_attribute', "code"), # values: PLOUGHLESS, DIRECT_SOWING
            ('land_use_restriction_type', "code"),
        ],        
        "FertilizationRecommendation":[
            # 10. Fertilization Recommendation
            ('crops', "asbie"),
            ('agent', "asbie"),
            ('form_of_fertilizer', "asbie"),
            ('substance_contained', "text"),  # provide a list of content as delimieted string
            ('fertilizer', "asbie"),
            ('application_quantity', "number"),
            ('application_measured_unit', "code"),            
        ],
        "SampleBase":[
            # 11. Sample @ base sample definition for soil and fertilizer samples
            ('recieved_date', "date_"),
            ('received_time', "time_"),
            ('description', "text"),
            ('comment', "text"),
            ('weight', "number"), 
            ('weight_unit', "code"),
            ('volume', "number"),
            ('volume_unit', "code"),
            ('composition', "text"),  # delimited string list
            ('information_source', "text"),  # name of agency performing test
            ('source_certificate', "text"),  # certification number or id for agency
            ('concentration', "text"), # delimited string list of composed substance and their measurements
            ('analysis_date', "date_"),
            ('analysis_time', "time_"),
        ],
        "SoilSample":[
            # 12. Soil sample @extends Sample
            ('soil_name', "text"),  # Give (alternative) name to soil type where not available in code
            ('soil_type', "code"),
            ('reference_part_of_field', "text"),
            ('spatial_data', "text"),
            ('referenced_field', "asbie"),  # references the field segment on farm
            ('depth', "number"),
            ('depth_unit', "code"),
            ('depth_range', "text"),
            ('analysis_method', "text"),
            ('soil_heaviness', "text"),
            ('soil_nutrient_classification', "text"),
            ('soil_texture', "text"),
        ],
        "AnalysisResult":[
            # 13. Analysis Result
            ('abstract_analysis', "text"),
            ('parameters', "text"),  # delimited string list. e.g {'PH_VALUE': ("method", "value", "classification" )}
            ('description', "text"),
            ('method', "text"),
            ('comment', "text"),
            ('sample', "asbie"),            
        ],
        "FertilizerSample":[
            # 14. Fertilizer sample @extends Sample
            ('fertilizer', "asbie"),            
        ],
        "Fertilizer":[
            # 15. Fertilizer
            ('fertilizer_brand', "text"),  # general market brand name
            ('fertlizer_name', "text"),  # specific manufacturer name
            ('fertilizer_type', "code"),
            ('fertilizer_manufacturer', "asbie"),  # the registered manufacturer in database of text for others
            ('supplier', "asbie"),  # the agent supplying fertilizer
            ('fertilizer_form', "text")
        ],
        "FieldCultivation":[
            # 16. Field Cultivation
            ('field', "asbie"),
            ('reference_field_part', "asbie"),
            ('duration_of_use', "number"),
            ('duration_unit', "code"),                        
        ],
        "Crop":[
            # 18. Crop
            ('field', "asbie"),
            ('monetary_value_per_hectar', "number"),
            ('monetary_value_currency', "code"),
            ('crop_growth_event', "asbie"),
            ('botanical_name', "name"),
            ('cultural_name', "name"),
            ('description', "text"),
        ],
        "CropGrowthStage":[
            # 19. Crop Growth Stage
            ('growth_stage', "text"),
            ('"date_"recorded', "date_"),
            ('time_recorded', "time_"),
            ('observer', "text"),  # reference unique id of user that observed growth or name of agent/3rd party
            ('reported_by', "asbie"),  # user reporting growth stage
            
        ],
        "CropSpecies":[
            # 20. Crop Species
            ('crop', "asbie"),
            ('name', "text"),
            ('variety', "code"),
            ('genetically_modified_organism', "boolean"),            
        ],
        "Harvest":[
            # 21. Harvest
            ('crop', "asbie"),
            ('harvested_quantity', "number"),
            ('yield_quantity', "number"),
            ('quantity_unit', "code"),
            # The code or string repr which can be parsed by target enum type.
            # The enum will have a default OTHER for cases not yet identified
            # Enum flag OTHER will enable collection and processing user's text data
            ('harvest_quality', "code"),
            ('field', "asbie"),
            ('start_date', "date_"),
            ('end_date', "date_")            
        ],
        "Activity":[
            # 22. Activity
            ('daily_start', "datetime_"),
            ('daily_end', "datetime_"),
            ('activity', "text"),
            ('comment', "text"),
            ('work_done', "text"),
            ('percentage_executed', "number"),
            ('reference', "asbie")  # generic reference to Harvest, Cultivation and other farming activities
        ],
        "Weather":[
            # 23. Weather
            ('temperature', "number"),
            ('temperature_unit', "code"),
            ('wind_speed', "number"),
            ('wind_speed_unit', "code"),
            ('humidity', "number"),
            ('humidity_unit', "code"),
            ('precipitation', "number"),
            ('precipitation_unit', "code"),
            ('solar_radiation', "number"),
            ('solar_radiation_unit', "code"),
            ('reported_by', "asbie"),
  # can be weather station or 3rd party agent
            ('reported_date', "date_"),
            ('reported_time', "time_"),
            ('measured_date', "date_"),
  # use this field for weather condition measured by on farm
            ('measured_time', "time_"),
            ('measured_by', "asbie"),
        ],
        "Contamination":[
            # 24. Contamination
            ('contaimination_type', "text"),
            ('contamination_degree', "text"),
            ('noticed_date', "date_"),
            ('noticed_time', "time_"),
            ('reported_by', "asbie"),
            ('affected_fields', "asbie"),
            
        ],               
        "AgriculturalProgramme":[
            # 25. Agricultural Programme @e.g palm seedling donations
            ('start', "datetime_"),
            ('end', "datetime_"),
            ('invitations', "asbie"),
            ('consultants', "asbie"),
            ('purpose', "text"),
            ('description', "text"),
            ('kpis', "asbie"),
            ('targets', "text"),
            ('comments', "text"),
            ('status', "asbie"),
        ],
        "ProgrammePerformance":[
            # 26. Programme Performance
            ('participants','text' ),
 # actual record of participants as against invitation            
            ('programme_activities','text' ),
            ('comments', 'text'),
            ('learning_points', 'text'),
  # learning from the event by organisers
            ('recommendations', 'text'),
  # should hold organisers recommendations for later
            ('participant_suggestions','text' ),
 # should hold participant's suggestions/recommendations
            ('event_coverage', "binary"),  # uploaded photos or videos
            ('activity', "asbie")  # reference the generic activity model for daily activities
        ],
        "MeasuredKPI":[
            # 27. Measured KPI
            ('measured_kpis', "asbie"),
  # delimited text for the KPIs measured with their unit
            ('impact_assessment', "text"),
            ('programme_performance', "asbie")
        ]
}

