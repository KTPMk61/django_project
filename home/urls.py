from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('student_home/<int:idA>/<int:idS>/',views.student_home),
    path('studentinf/<int:idA>/<int:idS>/',views.studentinf),
    path('teacherview/<int:idA>/<int:idS>/',views.teacherview),
    path('viewclass/<int:idA>/<int:idS>/',views.viewclass),
    path('memcls/<int:idA>/<int:idS>/<int:idC>',views.memcls),
    path('viewinft/<int:idA>/<int:idT>/',views.viewinfteacher),
    path('teacher/<int:idA>/<int:idT>/',views.teacher),
    path('creatclass/<int:idA>/<int:idT>/',views.creatclass),
]