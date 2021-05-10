from django.db import models
from coursedetails.models import Coursedetails


# Create your models here.
class Studentdetails(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    course = models.ManyToManyField(Coursedetails, db_table='Courseenrollment')

    def __str__(self):
        return self.firstname

class Enrollment(models.Model):
    studentname = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
