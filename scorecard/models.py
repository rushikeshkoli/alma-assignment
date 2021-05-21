from django.db import models


# Create your models here.
class ScoreCard(models.Model):
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percentage = models.FloatField(default=0)


class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True, default=None)
    name = models.CharField(max_length=50, default=None)
    scorecard = models.ForeignKey(ScoreCard, on_delete=models.CASCADE, default=None)
