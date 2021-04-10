from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse
from .forms import MailStoreForm
from django.contrib import messages


class EmailSanderView(View):
    def get(self, request, *args, **kwargs):
        form = MailStoreForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = MailStoreForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                message = form.cleaned_data.get('message')
                # email sanding function start from here
                subject = 'Notifications'
                message = str(message)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail(subject, message, email_from, recipient_list)
                # email sanding function end here
                form.save()
                messages.success(request, "Your Email Sended Successfully!")
                return redirect('index')
        else:
            return HttpResponse('errors')

