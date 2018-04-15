from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('teacher/<int:id>/',views.teacher),
    path('student/<int:id>/', views.student),
    path('register/',views.reg),
    path('login/',views.login),
    path('score/<int:id>/',views.viewscore),
    path('class/<int:id>/',views.viewclass),
    path('viewinf/<int:id>/',views.viewinf),
    path('viewclasst/<int:id>/',views.viewclasst),
    path('update/<int:id>/',views.update),
    path('KTPM/<int:id>/',views.KTPM),
    path('SXTK/<int:id>/',views.SXTK),
    path('teacherinf/<int:id>/',views.teacherinf),
    path('searchst/<int:id>/',views.searchst)
]