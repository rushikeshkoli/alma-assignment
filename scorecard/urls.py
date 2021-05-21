from django.contrib import admin
from django.urls import path
from .views import hello, Result, LeaderBoard

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', hello),
    path('result/', Result.as_view()),
    path('leaderboard/', LeaderBoard.as_view()),
]