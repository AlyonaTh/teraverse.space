from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            # subject = f'Name {form.name} email: {form.email}'
            # send_mail(subject, form.message, form.email, ['tyoaa51@gmail.com'])
            # messages.success(request, 'Your message has been sent successfully!')
            return redirect(reverse_lazy('success_page'))
        else:
            # messages.error(request, 'An error occurred. Please try again.')
            return redirect(reverse_lazy('contact'))


class SendContact(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()

            send_mail(form.subject, f'{form.message} from {form.email}', 'tyoaa51@yandex.ru', ['tyoaa51@yandex.ru'])
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('contact')



class Success(View):
    def get(self, request):
        return render(request, 'success.html')


