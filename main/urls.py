from django.urls import path
from . import views

urlpatterns =[
    path('', views.redirect_to_projects, name='reditect_page'),
    path('projects/', views.show_projects, name='projects_page'),
]
