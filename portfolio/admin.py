from django.contrib import admin
from django.conf import settings
from .models import PersonalInfo, Experience, SkillCategory, Skill, Project

# Customize admin site
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', 'Ranjith Portfolio Admin')
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', 'Portfolio Admin Portal')
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', 'Welcome to Portfolio Administration')

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']
    search_fields = ['name', 'title', 'email']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'start_date']
    search_fields = ['title', 'company']
    ordering = ['-order', '-start_date']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category__order', 'order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order']
    list_filter = ['is_featured']
    search_fields = ['title', 'description']
    ordering = ['order']
