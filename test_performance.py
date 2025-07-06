#!/usr/bin/env python
"""
Performance Test Script for Django Portfolio
Tests page load times, database queries, and cache performance
"""

import time
from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from django.db import connection
from portfolio.models import PersonalInfo, Experience, SkillCategory, Project

def test_page_load_time():
    """Test main portfolio page load time"""
    print("🚀 Testing page load performance...")
    
    client = Client()
    start_time = time.time()
    
    # Test main portfolio page
    response = client.get(reverse('portfolio_home'))
    load_time = time.time() - start_time
    
    print(f"📊 Page load time: {load_time:.3f} seconds")
    print(f"📄 Response status: {response.status_code}")
    print(f"📦 Response size: {len(response.content)} bytes")
    
    if load_time < 2.0:
        print("✅ Excellent performance!")
    elif load_time < 3.0:
        print("✅ Good performance")
    else:
        print("⚠️  Performance needs improvement")
    
    return load_time

def test_database_queries():
    """Test database query performance"""
    print("\n🗄️ Testing database performance...")
    
    # Test query count
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM portfolio_personalinfo")
        personal_info_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM portfolio_experience")
        experience_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM portfolio_project")
        project_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM portfolio_skillcategory")
        skill_category_count = cursor.fetchone()[0]
    
    print(f"📊 Database records:")
    print(f"   - Personal Info: {personal_info_count}")
    print(f"   - Experiences: {experience_count}")
    print(f"   - Projects: {project_count}")
    print(f"   - Skill Categories: {skill_category_count}")
    
    # Test query performance
    start_time = time.time()
    personal_info = PersonalInfo.objects.select_related().first()
    query_time = time.time() - start_time
    
    print(f"⏱️  Personal info query time: {query_time:.4f} seconds")
    
    if query_time < 0.01:
        print("✅ Excellent query performance!")
    elif query_time < 0.1:
        print("✅ Good query performance")
    else:
        print("⚠️  Query performance needs optimization")
    
    return query_time

def test_cache_performance():
    """Test cache performance"""
    print("\n💾 Testing cache performance...")
    
    # Test cache set/get
    start_time = time.time()
    cache.set('test_key', 'test_value', 60)
    cache_value = cache.get('test_key')
    cache_time = time.time() - start_time
    
    print(f"⏱️  Cache operation time: {cache_time:.4f} seconds")
    
    if cache_value == 'test_value':
        print("✅ Cache working correctly")
    else:
        print("❌ Cache not working")
    
    # Clean up
    cache.delete('test_key')
    
    return cache_time

def test_static_files():
    """Test static file serving"""
    print("\n📁 Testing static file performance...")
    
    client = Client()
    
    # Test CSS file
    start_time = time.time()
    response = client.get('/static/portfolio/css/style.css')
    css_time = time.time() - start_time
    
    print(f"⏱️  CSS load time: {css_time:.4f} seconds")
    print(f"📦 CSS file size: {len(response.content)} bytes")
    
    # Test JS file
    start_time = time.time()
    response = client.get('/static/portfolio/js/main.js')
    js_time = time.time() - start_time
    
    print(f"⏱️  JS load time: {js_time:.4f} seconds")
    print(f"📦 JS file size: {len(response.content)} bytes")
    
    return css_time + js_time

def generate_performance_report():
    """Generate comprehensive performance report"""
    print("=" * 50)
    print("📊 PERFORMANCE TEST REPORT")
    print("=" * 50)
    
    # Run all tests
    page_load_time = test_page_load_time()
    db_query_time = test_database_queries()
    cache_time = test_cache_performance()
    static_time = test_static_files()
    
    # Calculate total performance score
    total_time = page_load_time + db_query_time + cache_time + static_time
    
    print("\n" + "=" * 50)
    print("📈 PERFORMANCE SUMMARY")
    print("=" * 50)
    print(f"📄 Page Load Time: {page_load_time:.3f}s")
    print(f"🗄️  Database Query Time: {db_query_time:.4f}s")
    print(f"💾 Cache Operation Time: {cache_time:.4f}s")
    print(f"📁 Static Files Time: {static_time:.4f}s")
    print(f"⏱️  Total Test Time: {total_time:.3f}s")
    
    # Performance recommendations
    print("\n🎯 RECOMMENDATIONS:")
    
    if page_load_time > 3.0:
        print("⚠️  Page load time is slow - consider:")
        print("   - Optimizing database queries")
        print("   - Implementing more caching")
        print("   - Compressing images")
    
    if db_query_time > 0.1:
        print("⚠️  Database queries are slow - consider:")
        print("   - Adding database indexes")
        print("   - Using select_related() and prefetch_related()")
        print("   - Implementing query caching")
    
    if static_time > 0.5:
        print("⚠️  Static files are slow - consider:")
        print("   - Using a CDN")
        print("   - Compressing static files")
        print("   - Implementing browser caching")
    
    # Overall score
    if total_time < 4.0:
        print("🎉 EXCELLENT: Your portfolio is performing well!")
    elif total_time < 6.0:
        print("✅ GOOD: Your portfolio has good performance")
    else:
        print("⚠️  NEEDS IMPROVEMENT: Consider the recommendations above")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    import os
    import sys
    import django
    
    # Add the project directory to Python path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    # Setup Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ranjith_portfolio.settings')
    django.setup()
    
    # Run performance tests
    generate_performance_report() 