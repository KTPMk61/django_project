from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('teacher/',views.teacher),
    path('student/<int:id>/', views.student),
    path('register/',views.reg),
    path('login/',views.login),
    path('score/<int:id>/',views.viewscore),
    path('class/<int:id>/',views.viewclass)

]