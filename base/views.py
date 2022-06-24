from django.shortcuts import redirect, render

from .models import Project
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings


def home(request):
    projects = Project.objects.order_by("id")[:3]
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')

    context = {'form': form,
               'projects': projects
               }
    return render(request, 'base/home.html', context)


def about(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email address is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')

    context = {
        'form': form
    }
    return render(request, 'base/about.html', context)


def services(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email address is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')

    context = {
        'form': form
    }
    return render(request, 'base/services.html', context)





def ContactMe(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email address is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')

    context = {'form': form}
    return render(request, 'contact-me.html', context)


def thankYou(request):
    return render(request, 'base/thank-you.html')


def ProjectArchiveView(request):
    projects = Project.objects.all()
    # paginator = Paginator(projects,4)
    form = ContactForm()

    # page=request.GET.get('page')
    # try:
    #     projects=paginator.page(page)
    # except PageNotAnInteger:
    #     projects=paginator.page(1)
    # except EmptyPage:
    #     projects=paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email address is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')

    context = {'form': form,
               'projects': projects
               }

    return render(request, 'base/project-archive.html', context)


def ProjectView(request, slug):
    project = Project.objects.get(slug=slug)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            send_mail(
                subject,
                message + "my email address is " + " " + email,
                settings.EMAIL_HOST_USER,
                ['dev.web.008@gmail.com', 'contact@kevinnyarango.com'],
                fail_silently=False
            )
            return redirect('/thank-you/')
    else:
        form = ContactForm()

    context = {
        'project': project,
        'form': form,
    }

    return render(request, 'base/project.html', context)
