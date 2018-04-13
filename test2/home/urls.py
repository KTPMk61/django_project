from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('teacher/',views.teacher),
    path('student/', views.student),
    path('register/',views.reg),
    path('login/',views.login),
    path('login/score/<int:id>/',views.viewscore)

]