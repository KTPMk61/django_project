from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('register/',views.reg),
    path('reg/student/',views.regs),
    path('reg/teacher/',views.regt),
]