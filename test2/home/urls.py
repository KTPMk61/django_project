from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('register/',views.reg),
    path('reg/student/',views.regs),
    path('reg/teacher/',views.regt),
    path('teacherinf/<int:idCls>/<int:id>/',views.teacherinf),
    path('student/<int:idCls>/<int:id>/',views.student),
    path('studentinf/<int:idCls>/<int:id>/', views.studentinf),
    path('studentclass/<int:idCls>/<int:id>/', views.viewclass),
    path('update/<int:idCls>/<int:id>/',views.update),
    path('teacher/<int:idCls>/<int:id>/', views.teacher),
    path('viewinf/<int:idCls>/<int:id>/', views.viewinf),
    path('searchst/<int:idCls>/<int:id>/',views.search),
    path('viewclasst/<int:idCls>/<int:id>/',views.viewclasst)
]