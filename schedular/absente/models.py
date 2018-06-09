# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy
from django.db import models
from users.models import User

disciplina_details = (
    (0, ugettext_lazy('curs')),
    (1, ugettext_lazy('laborator')),
    (2, ugettext_lazy('seminar'))
)

colors_details = (
    (0, ugettext_lazy('#cc4646')),
    (1, ugettext_lazy('#3b91ad')),
    (2, ugettext_lazy('#3bcc91'))
)

class SchoolObject(models.Model):
    disciplina = models.IntegerField(choices=disciplina_details)
    nume_obiect = models.CharField(
        max_length=40, null=True, blank=True,
        verbose_name=ugettext_lazy('Nume obiect'))
    profesor = models.ForeignKey(User)
    color = models.IntegerField(choices=colors_details, help_text="*Note: Curs->#cc4646 Laborator->#3b91ad  Seminar->#3bcc91")
    # color = models.CharField(
    #     max_length=40, null=True, blank=True,
    #     verbose_name=ugettext_lazy('Color'))

    def __unicode__(self):
        return u"{0}".format(self.nume_obiect)


class Absente(models.Model):
    student = models.ForeignKey(User)
    materie = models.ForeignKey(SchoolObject)
    start = models.DateTimeField()
    end = models.DateTimeField()
