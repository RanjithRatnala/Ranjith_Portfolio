from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os
from typing import List, Dict, Any, Optional
from .models import PersonalInfo, Experience, SkillCategory, Project


def portfolio_home(request):
    """Main portfolio view that renders the complete portfolio page"""
    try:
        context: Dict[str, Any] = {
            'personal_info': PersonalInfo.objects.first(),
            'experiences': Experience.objects.all().order_by('-start_date'),
            'skill_categories': SkillCategory.objects.prefetch_related('skills').order_by(
                'order'
            ),
            'projects': Project.objects.filter(is_featured=True).order_by('order'),
        }
        return render(request, 'portfolio/portfolio.html', context)
    except Exception:
        # Fallback to simple template if there's an issue
        context: Dict[str, Any] = {
            'personal_info': None,
            'experiences': [],
            'skill_categories': [],
            'projects': [],
        }
        return render(request, 'portfolio/simple.html', context)


def download_resume(request):
    """View to handle resume download"""
    personal_info: Optional[PersonalInfo] = PersonalInfo.objects.first()
    if personal_info and personal_info.resume_file:
        file_path = personal_info.resume_file.path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(
                    f.read(), content_type='application/pdf'
                )
                response['Content-Disposition'] = (
                    f'attachment; filename="{os.path.basename(file_path)}"'
                )
                return response
    return JsonResponse({'error': 'Resume not found'}, status=404)


def api_personal_info(request):
    """API endpoint for personal information"""
    personal_info: Optional[PersonalInfo] = PersonalInfo.objects.first()
    if personal_info:
        data: Dict[str, Any] = {
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


def api_experiences(request):
    """API endpoint for experience data"""
    experiences: List[Experience] = Experience.objects.all().order_by('-start_date')
    data: List[Dict[str, Any]] = []
    for exp in experiences:
        experience_data: Dict[str, Any] = {
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


def api_skills(request):
    """API endpoint for skills data"""
    categories: List[SkillCategory] = SkillCategory.objects.prefetch_related('skills').order_by('order')
    data: List[Dict[str, Any]] = []
    for category in categories:
        category_data: Dict[str, Any] = {
            'name': category.name,
            'skills': []
        }
        for skill in category.skills.all().order_by('order'):
            category_data['skills'].append({
                'name': skill.name,
                'proficiency': skill.proficiency
            })
        data.append(category_data)
    return JsonResponse({'skill_categories': data})


def api_projects(request):
    """API endpoint for projects data"""
    projects: List[Project] = Project.objects.filter(is_featured=True).order_by('order')
    data: List[Dict[str, Any]] = []
    for project in projects:
        project_data: Dict[str, Any] = {
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
