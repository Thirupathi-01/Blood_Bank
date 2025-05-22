# Blood Bank Management System

A web-based application for managing blood donors, blood requests, and inventory, built with Django.

## Features

- Register blood donors with details (name, age, phone, email, city, address, blood group, etc.)
- Add and manage blood inventory by blood type
- Request blood for patients, with automatic eligibility checks and email notifications to compatible donors
- Donor eligibility based on blood group compatibility and 90-day donation interval
- Admin interface for managing all data
- Clean, responsive UI for all major pages
- **In Progress:** Machine Learning algorithm to use donor location coordinates to find and notify the nearest eligible donors if no one is available in the requested city

## Setup Instructions

1. Clone the repository
   git clone https://github.com/Thirupathi-01/Blood_Bank.git
   cd Blood_Bank
   

2. Create a virtual environment and activate it
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
  

3. **Install dependencies**
   pip install django
   
4. Apply migrations
   python manage.py makemigrations
   python manage.py migrate
   

5. Create a superuser (for admin access)
   python manage.py createsuperuser
   

6. Run the development server
   sh
   python manage.py runserver
   

7. Access the application
   - Main site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

 Configuration

 To enable email notifications, configure your email backend in `settings.py`.

## Project Structure

- BB/ - Main Django app (models, views, forms, templates, static files)
- BLOODBANK/ - Django project settings and URLs
- templates/ - Shared base templates
- static/ - CSS and images
