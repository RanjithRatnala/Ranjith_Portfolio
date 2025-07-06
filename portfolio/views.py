from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import os
from .models import PersonalInfo, Experience, SkillCategory, Skill, Project

@cache_page(60 * 15)  # Cache for 15 minutes
def portfolio_home(request):
    """Main portfolio view that renders the complete portfolio page"""
    try:
        # Use select_related and prefetch_related for optimized queries
        context = {
            'personal_info': PersonalInfo.objects.select_related().first(),
            'experiences': Experience.objects.select_related().all().order_by('-start_date'),
            'skill_categories': SkillCategory.objects.prefetch_related('skills').order_by('order'),
            'projects': Project.objects.filter(is_featured=True).order_by('order'),
        }
        return render(request, 'portfolio/portfolio.html', context)
    except Exception as e:
        # Fallback context if there are any issues
        context = {
            'personal_info': None,
            'experiences': [],
            'skill_categories': [],
            'projects': [],
        }
        return render(request, 'portfolio/portfolio.html', context)

def download_resume(request):
    """View to handle resume download"""
    try:
        personal_info = PersonalInfo.objects.first()
        if personal_info and personal_info.resume_file:
            # Get the file path
            file_path = personal_info.resume_file.path
            if os.path.exists(file_path):
                # Open and read the file
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                    return response
            else:
                return JsonResponse({'error': 'Resume file not found on disk'}, status=404)
        return JsonResponse({'error': 'Resume not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Error downloading resume: {str(e)}'}, status=500)

@cache_page(60 * 30)  # Cache for 30 minutes
def api_personal_info(request):
    """API endpoint for personal information"""
    try:
        personal_info = PersonalInfo.objects.select_related().first()
        if personal_info:
            data = {
                'name': personal_info.name,
                'title': personal_info.title,
                'description': personal_info.description,
                'email': personal_info.email,
                'phone': personal_info.phone,
                'location': personal_info.location,
                'github_url': personal_info.github_url,
                'linkedin_url': personal_info.linkedin_url,
            }
            if personal_info.profile_image:
                data['profile_image'] = personal_info.profile_image.url
            return JsonResponse(data)
        return JsonResponse({'error': 'Personal info not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Server error'}, status=500)

@cache_page(60 * 30)  # Cache for 30 minutes
def api_experiences(request):
    """API endpoint for experience data"""
    try:
        experiences = Experience.objects.select_related().all().order_by('-start_date')
        data = []
        for exp in experiences:
            experience_data = {
                'title': exp.title,
                'company': exp.company,
                'description': exp.description,
                'start_date': exp.start_date.strftime('%Y-%m-%d'),
                'is_current': exp.is_current,
            }
            if exp.end_date:
                experience_data['end_date'] = exp.end_date.strftime('%Y-%m-%d')
            data.append(experience_data)
        return JsonResponse({'experiences': data})
    except Exception as e:
        return JsonResponse({'error': 'Server error'}, status=500)

@cache_page(60 * 30)  # Cache for 30 minutes
def api_skills(request):
    """API endpoint for skills data"""
    try:
        categories = SkillCategory.objects.prefetch_related('skills').order_by('order')
        data = []
        for category in categories:
            category_data = {
                'name': category.name,
                'skills': []
            }
            # Django creates this relationship automatically via related_name='skills'
            for skill in category.skills.all().order_by('order'):  # type: ignore
                category_data['skills'].append({
                    'name': skill.name,
                    'proficiency': skill.proficiency
                })
            data.append(category_data)
        return JsonResponse({'skill_categories': data})
    except Exception as e:
        return JsonResponse({'error': 'Server error'}, status=500)

@cache_page(60 * 30)  # Cache for 30 minutes
def api_projects(request):
    """API endpoint for projects data"""
    try:
        projects = Project.objects.filter(is_featured=True).order_by('order')
        data = []
        for project in projects:
            project_data = {
                'title': project.title,
                'description': project.description,
                'technologies': project.get_technologies_list(),
                'live_url': project.live_url,
                'github_url': project.github_url,
            }
            if project.image:
                project_data['image'] = project.image.url
            data.append(project_data)
        return JsonResponse({'projects': data})
    except Exception as e:
        return JsonResponse({'error': 'Server error'}, status=500)
