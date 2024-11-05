# emailer/views.py

import csv
import io
import time
import os
from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadCSVForm  # Ensure your form is defined

def send_bulk_email_view(request):
    error_messages = []

    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            recipient_list = []
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')
            for row in reader:
                recipient_list.append(row[0])  # Assuming emails are in the first column

            subject = request.POST.get('subject', 'Default Subject')
            message = request.POST.get('message', 'Default Message')

            total_emails = len(recipient_list)
            sent_emails = 0
            failed_emails = []
            successful_emails = []

            for email in recipient_list:
                try:
                    send_mail(
                        subject,
                        message,
                        'manish@videcreators.com',  # Your verified sender email
                        [email],
                        fail_silently=False,
                    )
                    sent_emails += 1
                    successful_emails.append(f"{email} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  # Add timestamp
                    time.sleep(0.5)  # Adjust delay as needed for rate limiting
                except Exception as e:
                    error_message = f"Error sending email to {email}: {e}"
                    error_messages.append(error_message)  # Capture the error message
                    failed_emails.append(f"{email} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  # Add timestamp

            # Write successful emails to a file
            with open('successful_emails.txt', 'w') as success_file:
                for entry in successful_emails:
                    success_file.write(f"{entry}\n")

            # Write failed emails to a file
            with open('failed_emails.txt', 'w') as fail_file:
                for entry in failed_emails:
                    fail_file.write(f"{entry}\n")

            return JsonResponse({
                'total': total_emails,
                'sent': sent_emails,
                'errors': error_messages
            })

    else:
        form = UploadCSVForm()

    return render(request, 'emailer/upload.html', {
        'form': form,
        'error_messages': error_messages  # Pass errors to the template
    })
