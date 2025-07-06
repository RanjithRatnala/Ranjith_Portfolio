# Render Deployment Guide

This guide will help you deploy your Django portfolio to Render.com

## Prerequisites

- GitHub account
- Render account (free tier available)
- Your code pushed to GitHub

## Step 1: Prepare Your Repository

### 1.1 Push to GitHub
```bash
git init
git add .
git commit -m "Production-ready Django portfolio for Render"
git remote add origin https://github.com/yourusername/ranjith-portfolio.git
git push -u origin main
```

### 1.2 Verify Files
Ensure these files are in your repository:
- ✅ `requirements.txt`
- ✅ `render.yaml` (for automated setup)
- ✅ `build.sh` (build script)
- ✅ `manage.py`
- ✅ All Django app files

## Step 2: Deploy to Render

### Option A: Automated Setup (Recommended)

1. **Go to [Render Dashboard](https://dashboard.render.com/)**
2. **Click "New" → "Blueprint"**
3. **Connect your GitHub repository**
4. **Select the repository with your Django project**
5. **Click "Connect"**
6. **Review the configuration** (it will use your `render.yaml`)
7. **Click "Apply"**

Render will automatically:
- Create a PostgreSQL database
- Create a web service
- Set up environment variables
- Deploy your application

### Option B: Manual Setup

#### 2.1 Create PostgreSQL Database
1. Go to Render Dashboard
2. Click "New" → "PostgreSQL"
3. Name: `portfolio-db`
4. Database: `portfolio_db`
5. User: `portfolio_user`
6. Click "Create Database"
7. Copy the **Internal Database URL**

#### 2.2 Create Web Service
1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: `ranjith-portfolio`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn Ranjith_Portfolio.wsgi:application`
   - **Health Check Path**: `/health/`

#### 2.3 Set Environment Variables
Add these in the Render dashboard:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-service.onrender.com` |
| `DATABASE_URL` | (Internal Database URL from step 2.1) |
| `REDIS_URL` | `redis://localhost:6379` |
| `EMAIL_BACKEND` | `django.core.mail.backends.console.EmailBackend` |
| `DEFAULT_FROM_EMAIL` | `noreply@your-service.onrender.com` |

## Step 3: Post-Deployment Setup

### 3.1 Run Migrations
After deployment, go to your web service → "Shell" and run:
```bash
python manage.py migrate
```

### 3.2 Create Superuser
```bash
python manage.py createsuperuser
```

### 3.3 Add Content
1. Go to `https://your-service.onrender.com/admin/`
2. Log in with your superuser credentials
3. Add your portfolio content:
   - Personal Information
   - Experience
   - Skills and Skill Categories
   - Projects

## Step 4: Custom Domain (Optional)

1. Go to your web service settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records as instructed
5. Update `ALLOWED_HOSTS` to include your domain

## Step 5: SSL Certificate

Render automatically provides SSL certificates for all services.

## Troubleshooting

### Common Issues

#### 1. Build Failures
- Check that all dependencies are in `requirements.txt`
- Ensure `render.yaml` syntax is correct
- Verify Python version compatibility

#### 2. Database Connection Issues
- Verify `DATABASE_URL` is correct
- Check that database is created and running
- Ensure migrations are run

#### 3. Static Files Not Loading
- Verify `collectstatic` runs during build
- Check WhiteNoise configuration
- Ensure `STATIC_ROOT` is set correctly

#### 4. Health Check Failures
- Verify `/health/` endpoint returns 200
- Check that `ALLOWED_HOSTS` includes your domain
- Ensure application starts successfully

### Debug Commands

In Render Shell:
```bash
# Check logs
tail -f /opt/render/project/src/logs/django.log

# Test database
python manage.py dbshell

# Check environment
env | grep DJANGO

# Test static files
ls -la /opt/render/project/src/staticfiles/
```

## Performance Optimization

### 1. Database Optimization
```bash
python manage.py optimize_db
```

### 2. Cache Management
```bash
python manage.py cache_clear
```

### 3. Static Files
- WhiteNoise handles compression automatically
- Files are served with proper cache headers

## Monitoring

### 1. Render Dashboard
- Monitor uptime and performance
- View logs in real-time
- Check resource usage

### 2. Health Checks
- Render automatically checks `/health/`
- Set up external monitoring if needed

### 3. Logs
- Access logs via Render dashboard
- Set up log aggregation if needed

## Security

### 1. Environment Variables
- Never commit secrets to Git
- Use Render's environment variable system
- Rotate secrets regularly

### 2. Database Security
- Render manages PostgreSQL security
- Use connection pooling for performance
- Regular backups are automatic

### 3. Application Security
- DEBUG=False in production
- HTTPS enforced automatically
- Security headers configured

## Cost Optimization

### Free Tier Limits
- 750 hours/month for web services
- 90 days for databases
- 1GB storage per service

### Paid Plans
- $7/month for always-on web service
- $7/month for persistent database
- Additional storage and bandwidth

## Support

- [Render Documentation](https://render.com/docs)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Render Community](https://community.render.com/)

---

**Your Django portfolio is now ready for Render deployment!** 🚀 