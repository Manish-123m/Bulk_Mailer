# emailer/urls.py

from django.urls import path
from .views import send_bulk_email_view

urlpatterns = [
    path('', send_bulk_email_view, name='send_bulk_email'),  # URL for the bulk email sender view
]
