# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

PROGRAM_STUDY = (
    (0, ugettext_lazy('Licenta')),
    (1, ugettext_lazy('Masterat'))
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(
            username=username,
            is_staff=False, is_active=True, is_superuser=False,
            **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user_x = self.create(**extra_fields)
        user_x.email = email
        user_x.set_password(password)
        user_x.is_active = True
        user_x.is_superuser = True
        user_x.is_staff = True
        user_x.save()
        return user_x


class User(AbstractBaseUser):
    first_name = models.CharField(
        max_length=30, null=True, blank=True,
        verbose_name=ugettext_lazy('first name'))
    last_name = models.CharField(
        max_length=30, null=True, blank=True,
        verbose_name=ugettext_lazy('last name'))
    email = models.EmailField(
        max_length=255, unique=True, db_index=True, null=True, blank=True,
        verbose_name=ugettext_lazy('email address'))
    username = models.CharField(
        max_length=255, unique=True, db_index=True, null=True, blank=True,
        verbose_name=ugettext_lazy('username'))
    address = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name=ugettext_lazy('address'))
    phone_number = models.CharField(
        max_length=25, blank=True, verbose_name=ugettext_lazy('phone number'))
    CNP = models.CharField(
        max_length=25, blank=True, verbose_name=ugettext_lazy('CNP'))
    second_email = models.EmailField(
        max_length=255, unique=True, db_index=True, null=True, blank=True,
        verbose_name=ugettext_lazy('second email address'))
    date = models.DateField(null=True, blank=True)
    graduation = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return u"{0} {1} ({2})".format(
            self.first_name, self.last_name, self.email)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return u"{0} {1}".format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return None

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

    def has_perm(self, obj):
        return True

    def get_short_name(self):
        return self.email