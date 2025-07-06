from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path('api/personal-info/', views.api_personal_info, name='api_personal_info'),
    path('api/experiences/', views.api_experiences, name='api_experiences'),
    path('api/skills/', views.api_skills, name='api_skills'),
    path('api/projects/', views.api_projects, name='api_projects'),
] 