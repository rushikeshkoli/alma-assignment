from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models


# Create your views here.

def hello(request):
    return HttpResponse('hello')


class Result(APIView):

    def post(self, request):
        data = request.data
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        maths = data['maths']
        chemistry = data['chemistry']
        total = maths + physics + chemistry
        percentage = round(total / 300, 2)
        student = models.Student.objects.get(roll_no=roll_no)
        if student:
            scorecard = models.ScoreCard.objects.get(student=student)
            scorecard.maths = maths
            scorecard.physics = physics
            scorecard.chemistry = chemistry
            scorecard.total = total
            scorecard.percentage = percentage
            scorecard.save()
        else:
            new_student = models.Student.objects.create(roll_no=roll_no, name=name)
            models.ScoreCard.objects.create(student=new_student, maths=maths, physics=physics, chemistry=chemistry,
                                            total=total, percentage=percentage)


class LeaderBoard(APIView):

    def get(self):
        students = models.Student.objects.get()
        scoreboard = []
        for student in students:
            scores = models.ScoreCard.objects.get(student=student)
            scoreboard.append({'name': student.name, 'roll_no': student.roll_no, 'physics': scores.physics,
                               'chemistry': scores.chemistry, 'maths': scores.maths, 'total': scores.total,
                               'percentage': scores.percentage})
        return Response({'scoreboard': scoreboard})
