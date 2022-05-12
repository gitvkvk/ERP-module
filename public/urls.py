from django.urls import path
from . import views

urlpatterns = [
         path('', views.indexpublic, name='indexpublic'),
         path('careers', views.careers, name='careers'),
         path('projects', views.projects, name='projects'),
         path('contactus', views.contactus, name='contactus'),

]

