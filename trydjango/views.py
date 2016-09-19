from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import Contact_form, sing_up_form
from .models import singup


def home(request):
    title = 'Зарегистрироваться'
    form = sing_up_form(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

        if request.user.is_authenticated11() and request.user.is_staff:
            queryset = singup.objects.all()
            context = {
                "queryset": queryset
            }

    return render(request, 'home.html', context)


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = Contact_form(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #    print(key)

        form_full_name = form.cleaned_data.get("full_name")
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        # print(email, message, full_name)
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@gmail.com']
        contact_message = "%s: %s via %s" % (
            form_full_name,
            form_email,
            form_message
        )
        some_html_message = """
        <h1>hello</h1>
        """
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  html_message=some_html_message,
                  fail_silently=True)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)


def about(request):
    return render(request, 'about.html', {})
