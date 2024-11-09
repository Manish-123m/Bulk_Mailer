# myemailproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', include('emailer.urls')),  # Include emailer URLs
    path('', RedirectView.as_view(url='/send-email/', permanent=True)),  # Redirect root to email form
]
