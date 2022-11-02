from django.urls import re_path as url
from pixelmate import views

urlpatterns = [
    url(r'^signup$', views.signupApi),
    url(r'^login$', views.loginApi),
    url(r'^user$', views.userApi),
    url(r'^project$', views.projectCompletedApi),
    url(r'^ongoing$', views.projectOnGoingApi),
    url(r'^complete$', views.completeProjectApi),
    url(r'^task$', views.taskApi),
    url(r'^challenge$', views.challengeApi),
    url(r'^acceptChallenge$', views.acceptChallengeApi),
    url(r'^completeChallenge$', views.completeChallengeApi),
    url(r'^upload$', views.uploadApi),
]

# url(r'^login/([0-9]+)$', views.loginApi), sample
