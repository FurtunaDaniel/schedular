from django_cron import CronJobBase, Schedule
from django.utils.translation import ugettext
from django.contrib.sites.models import Site

from schedular.email import send_email

from users.models import CronSettings, User

settings_obj = CronSettings.objects.last()
when = settings_obj.when.strftime('%H:%M') if settings_obj else '10:00'


class SendEmailsCron(CronJobBase):
    RUN_AT_TIMES = [when]
    RETRY_AFTER_FAILURE_MINS = 5

    schedule = Schedule(
        run_at_times=RUN_AT_TIMES,
        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)

    code = 'users.send_emails_cron'    # a unique code

    def do(self):
        current_site = Site.objects.get_current().domain
        for user in User.objects.exclude(email=None):
            link = "http://{0}/users/edit-user/{1}".format(
                current_site, user.pk)
            send_email(
                subject=ugettext("[USV] USV statistics update profile"),
                receiver=user.email,
                email_template_name='emails/update-user.html',
                context={'link': link, 'user': user})
            print "Sent email to " + user.email
