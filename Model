from django.db import models

class Registration(models.Model):
    School_ID = models.IntegerField(max_length=20)
    School_Name = models.CharField(max_length=200)
    Max_Students = models.IntegerField(default=0)
    Date = models.DateTimeField('Reg_Date')
    def __unicode__(self):
        return u'%s' % (self.School_ID)

class Attendance(models.Model):
    Registration = models.ForeignKey(Registration)
    Date = models.DateTimeField('DATE')
    Attendance = models.IntegerField(default=0)
    def __unicode__(self):
        return u'%s %s' % (self.Registration, self.Date)


