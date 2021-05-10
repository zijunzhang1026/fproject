from django.db import models


# Create your models here.
class Coursedetails(models.Model):
    course_id = models.BigIntegerField(unique=True, primary_key=True, default=0)
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    code = models.IntegerField()
    department = models.CharField(max_length=500)
    instructor = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    studentname = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
