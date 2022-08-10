from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import Project
from .forms import ContactForm


def homepage(request):
    project = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': project})


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Message about form"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@alexv92.pythonanywhere.com',
                          ['alexej.92@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("home")

    form = ContactForm()
    return render(request, "portfolio/contact.html", {'form': form})
