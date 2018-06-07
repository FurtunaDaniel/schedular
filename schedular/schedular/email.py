from django.core.mail import send_mail
from django.template import loader
from .settings import EMAIL_HOST_USER


def send_email(subject, receiver, email_template_name, context={}):
    html_content = loader.render_to_string(email_template_name, context)
    import ipdb; ipdb.set_trace()
    if not receiver:
        return

    if isinstance(receiver, basestring):
        to = [receiver]
        send_mail(subject, html_content, "contact@usv.com", to, fail_silently=False)
    else:
        to = receiver
        for t in to:
            dest = [t]
            send_mail(subject, html_content, "contact@usv.com", dest, fail_silently=False)
    