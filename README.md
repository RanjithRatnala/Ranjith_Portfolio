# Ranjith Portfolio

A modern, responsive Django portfolio website with dynamic content management through Django admin.

## Features

- 🎨 Modern, responsive design with dark/light theme toggle
- 📱 Mobile-first approach with smooth animations
- 🎯 Dynamic content management through Django admin
- 📊 Skills visualization with progress bars
- 💼 Project showcase with image support
- 📄 Resume download functionality
- 🚀 Performance optimized with caching
- 🔒 Production-ready security settings

## Tech Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Animations**: GSAP (GreenSock)
- **Icons**: Emoji-based theme toggle
- **Deployment**: Gunicorn + Nginx (recommended)

## Quick Start

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Ranjith_Portfolio
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Portfolio: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Configuration

### Development Settings

The project uses the default `settings.py` for development with:
- DEBUG = True
- SQLite database
- Local static file serving
- Basic security settings

### Production Settings

For production deployment, use `production_settings.py`:

```bash
export DJANGO_SETTINGS_MODULE=Ranjith_Portfolio.production_settings
python manage.py check --deploy
```

## Content Management

### Adding Content

1. **Access Django Admin**: http://localhost:8000/admin
2. **Create Personal Info**: Add your basic information
3. **Add Experience**: Create work experience entries
4. **Create Skill Categories**: Organize skills by category
5. **Add Skills**: Add individual skills with proficiency levels
6. **Add Projects**: Showcase your projects with images

### Content Structure

- **PersonalInfo**: Name, title, description, contact info, social links
- **Experience**: Work history with dates and descriptions
- **SkillCategory**: Groups for organizing skills (e.g., "Frontend", "Backend")
- **Skill**: Individual skills with proficiency percentages
- **Project**: Project showcase with images and links

## Deployment

### Production Checklist

- [ ] Set DEBUG = False
- [ ] Generate new SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up PostgreSQL database
- [ ] Configure static file serving
- [ ] Set up HTTPS/SSL
- [ ] Configure logging
- [ ] Set up caching (Redis recommended)
- [ ] Configure email settings
- [ ] Set up monitoring

### Deployment Options

#### Option 1: Traditional VPS

1. **Server Setup**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip nginx postgresql redis-server
   ```

2. **Application Setup**
   ```bash
   git clone <repository-url>
   cd Ranjith_Portfolio
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Database Setup**
   ```bash
   sudo -u postgres createdb portfolio_db
   sudo -u postgres createuser portfolio_user
   ```

4. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

5. **Gunicorn Setup**
   ```bash
   pip install gunicorn
   gunicorn --bind 0.0.0.0:8000 Ranjith_Portfolio.wsgi:application
   ```

#### Option 2: Platform as a Service

- **Heroku**: Use `Procfile` and `runtime.txt`
- **Railway**: Direct Git deployment
- **Render**: Automatic deployment from Git
- **DigitalOcean App Platform**: Managed deployment

### Environment Variables

Create a `.env` file for production:

```env
DEBUG=False
SECRET_KEY=your-secure-secret-key
DATABASE_URL=postgresql://user:password@host:port/dbname
REDIS_URL=redis://localhost:6379/1
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Performance Optimization

### Implemented Optimizations

- ✅ Database query optimization with `select_related` and `prefetch_related`
- ✅ Template caching in production
- ✅ Static file compression
- ✅ Image optimization
- ✅ CSS/JS minification
- ✅ Browser caching headers
- ✅ Database connection pooling

### Additional Recommendations

- Use CDN for static files
- Implement Redis caching for API responses
- Optimize images with WebP format
- Use lazy loading for images
- Implement service worker for offline support

## Security

### Implemented Security Measures

- ✅ CSRF protection
- ✅ XSS protection headers
- ✅ Content type sniffing protection
- ✅ Frame options (X-Frame-Options)
- ✅ HTTPS redirect in production
- ✅ Secure cookie settings
- ✅ HSTS headers

### Additional Security Recommendations

- Regular security updates
- Database backup strategy
- SSL certificate management
- Rate limiting implementation
- Input validation and sanitization

## Troubleshooting

### Common Issues

1. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

2. **Database connection errors**
   - Check database settings
   - Ensure PostgreSQL is running
   - Verify connection credentials

3. **Migration errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Permission errors**
   ```bash
   chmod +x manage.py
   sudo chown -R www-data:www-data /path/to/project
   ```

### Debug Mode

For development debugging:

```python
# In settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

## API Endpoints

The portfolio includes REST API endpoints:

- `GET /api/personal-info/` - Personal information
- `GET /api/experiences/` - Work experience data
- `GET /api/skills/` - Skills and categories
- `GET /api/projects/` - Featured projects
- `GET /download-resume/` - Resume download

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Contact: [your-email@domain.com]
- Documentation: [link-to-docs]

---

**Note**: This is a production-ready Django portfolio application. Make sure to customize the content, styling, and configuration according to your needs before deployment. 