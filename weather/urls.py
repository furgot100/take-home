from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path('', views.index, name='index'),
    path('vote', views.vote, name="vote"),
    path('result/',views.results, name='result')
]