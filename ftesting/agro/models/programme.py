

class Event(BaseModel):    	
    event_comment = TextField(**text_default)
    event_start = DateTimeField(**date_default)    
    event_end = DateTimeField(**date_default)    
    observer = ForeignKey(User, on_delete=models.CASCADE, related_name="event_observer",) # defaults to user reporting event
    performer = ForeignKey(User, on_delete=models.CASCADE, related_name="events_performer", null=True)

    class Meta:
        abstract = True

class ProgrammePerformance(Event):	
    participants = TextField(**text_default)
    program_activities = TextField(**text_default)
    learning_points = TextField(**text_default)
    recommendations = TextField(**text_default)
    participants_suggestions = TextField(**text_default)    

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agric_programme:programme_performance:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agric_programme:programme_performance:update', args=(self.pk,))	
		
		
class AgriculturalProgramme(BaseModel):	
    comments = TextField()    
    targets = TextField()
    description = TextField()
    programme_start = DateTimeField()		
	programme_end = DateTimeField()
    purpose = TextField()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agric_programme:agricultural_programme:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agric_programme:agricultural_programme:update', args=(self.pk,))
		
		
class ProgrammePerformance(BaseModel):	
	participants = ManyToManyField(User, through='Participation') # actual record of participants as against invitation            
	programme = ForeignKey('agricultural_programme.AgriculturalProgramme', on_delete=models.CASCADE)
	programme_activities = ManyToManyField('Activity')  # reference the generic activity model	
	learning_points = TextField(**text_default)  # learning from the event by organisers
	recommendations = CharField(**text_default)  # should hold organisers recommendations for later
	event_coverage = FileField()  # uploaded photos or videos


class Participation(BaseModel):	
	programme_performance = ForeignKey('ProgrammePerformance')
	participant = ForeignKey(User)
	participant_suggestions = CharField(**text_default)  # should hold participants suggestions/recommendations
	recommendations = CharField(**text_default)  # should hold organisers recommendations for later	
	comments = TextField(**text_default)
	participant_coverage = FileField()
	
	
class MeasuredKPI(BaseModel):	
	measured_kpis = TextField()  # delimited name for the KPIs measured with their unit
	impact_assessment = TextField(**text_default)
	programme = ForeignKey('AgriculturalProgramme')


class DailyTask(Event):	
	activity = ForeignKey('Activity', on_delete=models.CASCADE)
	description = TextField()
	assigned_to = CharField(**name_default)  # identifier or name of the staff assigned
	performance_started_at = DateTimeField()  # the date and time the task was performed
	performance_ended_at = DateTimeField()
	status = CharField(**code_default)


class Activity(BaseModel):	
	activity = TextField()
    comment = TextField()
    percentage_executed = DecimalField(**decimal_default)    
    work_done = TextField()
	
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('agric_programme:activity:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('agric_programme:activity:update', args=(self.pk,))
		
		

