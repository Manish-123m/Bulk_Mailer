"# Bulk_Mailer" 
"# Bulk_Mailer"

Bulk Emailer using Python & Django

Overview

This project is a Bulk Emailer system built with the Django framework. It allows users to send bulk emails to a list of recipients. The application provides a web interface to manage email lists, create email templates, and schedule or send emails to multiple recipients at once.

Features
Email Template Management: Create and manage email templates for recurring messages.
Bulk Email Sending: Send bulk emails to a list of recipients.
Recipient Management: Upload, store, and manage recipient lists (CSV or manual entry).
Email Scheduling: Schedule emails to be sent at a later time.
Asynchronous Processing: Uses background tasks (via Celery) to send emails in the background for improved performance.
Authentication: Secure user access with Django’s user authentication system.
HTML and Plain Text Email Support: Send both HTML and plain-text emails.
Error Logging: Log errors for tracking and debugging issues with email delivery.
Tech Stack
Backend: Python 3.x, Django 4.x
Frontend: HTML, CSS, JavaScript (for basic UI)
Database: SQLite (default for development), PostgreSQL (production-ready)
Email Service: SMTP (configured with Gmail, SendGrid, or any other email provider)
Task Queue: Celery (for asynchronous task processing)
Queue Broker: Redis (for Celery)
Dependencies: Django, Celery, Redis, Django Allauth (for user authentication), Celery-Progress (optional, for progress bars)
Installation
Prerequisites
Python 3.x
Django 4.x
Redis (for Celery task queue)
An SMTP server (e.g., Gmail, SendGrid, etc.)
Steps to Install
Clone the repository:
git clone https://github.com/Manish-123m/Bulk_Mailer
cd bulk_mailer
Create a virtual environment:
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Set up environment variables: Create a .env file in the root directory and configure the necessary settings, like SMTP details and Celery settings:
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-email-password
CELERY_BROKER_URL=redis://localhost:6379/0
Set up the database:
Run migrations to set up the database schema.
python manage.py migrate
Create a superuser (for admin access):
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Start the Celery worker (for background email sending): In a new terminal window:
celery -A bulk_mailer worker --loglevel=info
Start the Redis server:
If Redis is not installed, install it and start the Redis server:
redis-server
Configuration
Email Settings: Update settings.py with your email backend configuration (SMTP server, login credentials, etc.).
Example (for Gmail SMTP):
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
Celery Configuration: Make sure you have the necessary Celery configurations in settings.py:
CELERY_BROKER_URL = 'redis://localhost:6379/0'
Usage
Admin Interface:
Go to http://127.0.0.1:8000/admin/ to log in as the superuser.
Here you can manage Email Templates, Recipient Lists, and Sent Emails.
Create and Manage Templates:
In the admin interface, navigate to Email Templates and create a new template.
Templates can be designed using both HTML and plain text.
Upload Recipients:
You can upload recipients in bulk via a CSV file containing names and email addresses.
Alternatively, add recipients manually via the admin panel or user interface.
Sending Bulk Emails:
Go to the Bulk Email Sending section in the UI to select a template, a recipient list, and customize the subject/message.
You can choose to send emails immediately or schedule them for a later time.
Task Monitoring:
View email send progress and any errors through the Email Logs.
Track asynchronous tasks in Celery (check the worker logs).
Example Email Template
html

<html>
  <body>
    <h1>Hello {{ recipient_name }}!</h1>
    <p>We're excited to inform you about our new product launch.</p>
    <p>Best regards,<br>Your Company</p>
  </body>
</html>

Asynchronous Email Sending with Celery
Celery is used for sending emails asynchronously in the background. This allows the application to handle large volumes of email sending without blocking the main application thread.
To send emails in the background, the task is queued in Redis, and the Celery worker processes the tasks. This helps avoid timeout errors and speeds up the email sending process for large lists.
Error Logging & Notifications
Errors related to sending emails are logged in the Django logs and can be monitored through the admin interface.
Notifications about failed email deliveries (e.g., due to invalid email addresses) can be sent to administrators.
Testing
Unit Tests: The project includes basic unit tests to ensure the functionality works as expected. You can run tests with:
python manage.py test
Contribution
Contributions are welcome! Feel free to fork this repository and create a pull request with your improvements.
Guidelines
Ensure that any new feature is well-documented in this README.
Make sure that any new functionality is covered by tests.
If you fix a bug, please reference the issue number in your pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Troubleshooting
Issue: Celery not processing emails
Solution: Ensure that Redis is running, and the Celery worker is started correctly with celery -A bulk_mailer worker --loglevel=info.
Issue: Email not sent
Solution: Check the logs in django.log or Celery worker logs for errors. Ensure that SMTP configuration is correct.
Issue: Redis connection issue
Solution: Ensure that Redis is installed and running. If Redis is down, Celery will not work correctly.
