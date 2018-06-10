from django.core.mail import send_mail
from django.template import loader
from .settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST
from .forms import EmailForm
from django.http import HttpResponse
from django.shortcuts import render

def send_email(request, context={}):
    # html_content = loader.render_to_string("emails/add-user.html", context)
    # receiver = "soiman.andrei@yahoo.com"
    # if not receiver:
    #     return
    form = EmailForm(request.POST)
    subject = form.data['subject']
    email = str(form.data['email_prof'])
    to = [email]
    send_mail("Probleme Absente", subject, email, to, fail_silently=False)
    return render(request, "users/student_details.html", {
        "student": request.user
    })