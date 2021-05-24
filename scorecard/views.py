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
        roll_no = int(data['roll_no'])
        name = data['name']
        physics = int(data['physics'])
        maths = int(data['maths'])
        chemistry = int(data['chemistry'])
        total = maths + physics + chemistry
        percentage = round((total / 300) * 100, 2)
        student = models.Student.objects.filter(roll_no=roll_no).exists()
        if student:
            scorecard = models.ScoreCard.objects.get(student=student)
            scorecard.maths = maths
            scorecard.physics = physics
            scorecard.chemistry = chemistry
            scorecard.total = total
            scorecard.percentage = percentage
            scorecard.save()
        else:
            scorecard = models.ScoreCard.objects.select_for_update().create(maths=maths, physics=physics, chemistry=chemistry,
                                                        total=total, percentage=percentage)
            models.Student.objects.create(roll_no=roll_no, name=name, scorecard=scorecard)
        return Response(status=200)


class LeaderBoard(APIView):

    def get(self, request):
        students = models.Student.objects.all()
        scoreboard = []
        for student in students:
            scores = models.ScoreCard.objects.get(id=student.scorecard_id)
            scoreboard.append({'name': student.name, 'roll_no': student.roll_no, 'physics': scores.physics,
                               'chemistry': scores.chemistry, 'maths': scores.maths, 'total': scores.total,
                               'percentage': scores.percentage})
        return Response({'scoreboard': scoreboard})
