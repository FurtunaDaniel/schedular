from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.conf.urls import url
from django.core.exceptions import PermissionDenied
from django.http import Http404

from django.utils.encoding import force_text
from django.utils.html import escape

from django.shortcuts import redirect
from django.template.response import TemplateResponse

from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserAdmin(admin.ModelAdmin):
    list_per_page = 25
    change_user_password_template = None
    add_form_template = 'users/add_form.html'
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'address',
                    'phone_number', 'is_superuser', 'action_anchors')

    fieldsets = [
        ('Date information about user', {'fields': [
            'first_name',
            'last_name',
            'email',
            'username',
            'address',
            'phone_number',
            'is_student',
            'is_teacher',
            'is_active',
            'is_staff',
            "is_superuser"
        ]

        }),

        ('Password', {
            'fields': ['password'],
            'classes': ['collapse']
        })
    ]

    add_fieldsets = (
        ('Date information about user', {
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2',
                'address',
                'phone_number',
                'is_student',
                'is_teacher',
                'is_active',
                'is_staff',
                'is_superuser'),
        }),
    )

    def action_anchors(self, object):
        url = reverse('admin:%s_%s_change' %
                      (object._meta.app_label, object._meta.model_name),
                      args=[object.id])
        return u'<a href="%s">Edit</a>' % (url)

    action_anchors.allow_tags = True
    action_anchors.short_description = ugettext('Actions')

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(UserAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(UserAdmin, self).get_form(request, obj, **defaults)

    def get_urls(self):
        return [
            url(r'^(.+)/password/$',
                self.admin_site.admin_view(self.user_change_password),
                name='auth_user_password_change'),
        ] + super(UserAdmin, self).get_urls()

    def user_change_password(self, request, id, form_url=''):
        if not self.has_change_permission(request):
            raise PermissionDenied
        user = self.get_object(request, unquote(id))
        if user is None:
            raise Http404(
                ('%(name)s object with primary key %(key)r does'
                    'not exist.') % {
                    'name': force_text(self.model._meta.verbose_name),
                    'key': escape(id),
                })
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(
                    request, form, None)

                self.log_change(request, user, change_message)
                msg = ugettext('Password changed successfully.')
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return redirect("/{0}/{1}/{2}/{3}/".format(
                    self.admin_site.name,
                    user._meta.app_label,
                    user._meta.model_name,
                    user.pk,
                ))
        else:
            form = self.change_password_form(user)
        if user.password:
            context = {
                'form': form,
                'is_popup': (
                    IS_POPUP_VAR in request.POST\
                    or IS_POPUP_VAR in request.GET),
                'opts': self.model._meta,
                'user': user,
            }
        else:
            context = {
                'is_popup': (IS_POPUP_VAR in request.POST or
                IS_POPUP_VAR in request.GET),
                'opts': self.model._meta,
                'user': user,
            }
        return TemplateResponse(
            request,
            self.change_user_password_template \
            or 'users/change_password.html', context)


admin.site.register(User, UserAdmin)
