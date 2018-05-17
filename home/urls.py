from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('student_home/<int:idA>/<int:idS>/',views.student_home),
    path('studentinf/<int:idA>/<int:idS>/',views.studentinf),
    path('teacherview/<int:idA>/<int:idS>/',views.teacherview),
]