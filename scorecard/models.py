from django.db import models


# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True),
    name = models.CharField,


class ScoreCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL),
    physics = models.IntegerField,
    chemistry = models.IntegerField,
    maths = models.IntegerField,
    total = models.IntegerField,
    percentage = models.IntegerField
