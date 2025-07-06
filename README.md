# Ranjith Portfolio - Django Portfolio Website

A dynamic portfolio website built with Django that allows you to manage your portfolio content through the Django admin panel.

## Features

- **Dynamic Content Management**: Add and edit your personal information, experience, skills, and projects through Django admin
- **Responsive Design**: Beautiful, modern design that works on all devices
- **Dark/Light Theme**: Toggle between dark and light themes
- **Smooth Animations**: GSAP-powered animations for a premium feel
- **Image Upload**: Upload profile pictures and project images
- **Resume Download**: Upload and serve your resume as a downloadable PDF

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser

```bash
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

- **Portfolio**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## Adding Your Content

### 1. Personal Information
- Go to Admin Panel → Personal Info
- Add your name, title, description, email, and other details
- Upload your profile picture and resume

### 2. Experience
- Go to Admin Panel → Experiences
- Add your work experience with company, title, description, and dates
- Set "Is Current" for your current position

### 3. Skills
- Go to Admin Panel → Skill Categories
- Create categories like "Frontend", "Backend", "Tools", etc.
- Go to Skills to add individual skills with proficiency percentages

### 4. Projects
- Go to Admin Panel → Projects
- Add your projects with descriptions, images, and links
- Add technologies as comma-separated values

## File Structure

```
Ranjith_Portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── Ranjith_Portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/
│   └── portfolio/
│       └── portfolio.html
├── static/
├── media/
└── db.sqlite3
```

## Customization

### Styling
The portfolio uses CSS custom properties for easy theming. You can modify the color scheme by editing the CSS variables in the template.

### Adding New Sections
To add new sections, you can:
1. Create new models in `portfolio/models.py`
2. Add corresponding admin configurations
3. Create views to handle the data
4. Update the template to display the new content

## Deployment

### Development
For local development, follow the setup instructions above.

### Render Deployment
For production deployment on Render, see the comprehensive guide:

📖 **[Render Deployment Guide](RENDER_DEPLOYMENT.md)**

This includes:
- Complete Render setup instructions
- PostgreSQL database configuration
- Environment variables setup
- Automated deployment with Blueprint
- Post-deployment configuration

### Quick Render Checklist
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] PostgreSQL database created on Render
- [ ] Environment variables configured
- [ ] Blueprint deployment completed
- [ ] Migrations and superuser created
- [ ] Portfolio content added

For detailed Render setup, refer to `RENDER_DEPLOYMENT.md`.

## Technologies Used

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript
- **Animations**: GSAP
- **Image Processing**: Pillow
- **Database**: SQLite (development), PostgreSQL (production recommended) 