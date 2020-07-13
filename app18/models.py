from django.db import models

class CourseModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    facultyname = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.IntegerField()


