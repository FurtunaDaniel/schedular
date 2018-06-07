from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_SUFFIX_LENGTH
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        max_length=254,
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        max_length=UNUSABLE_PASSWORD_SUFFIX_LENGTH,
        label='',
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class SearchStudent((forms.Form)):
    search = forms.CharField(
        max_length=20,
        label='',
    )


# class UniversityForm(forms.ModelForm):
#     class Meta:
#         model = University
#         fields = ('__all__')


class UserForm(forms.ModelForm):
    def __init__(self, request_user=None, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        if self.cleaned_data['email'] == "":
            raise forms.ValidationError("Please insert email.")

        if User.objects.filter(
            email=self.cleaned_data['email']).exclude(
                email=self.instance.email).exists():
            raise forms.ValidationError(
                "This email is used by another user.")

        return self.cleaned_data['email']

    def clean_first_name(self):
        if self.cleaned_data['first_name'] == "":
            raise forms.ValidationError("Please insert first name.")

        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if self.cleaned_data['last_name'] == "":
            raise forms.ValidationError("Please insert last name.")

        return self.cleaned_data['last_name']


class UserEditForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        max_length=UNUSABLE_PASSWORD_SUFFIX_LENGTH,
        label='',
    )
    password_conf = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        max_length=UNUSABLE_PASSWORD_SUFFIX_LENGTH,
        label='',
    )

    def __init__(self, request_user=None, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'address', 'phone_number', 'CNP',
                  'second_email', 'date', 'graduation')

    def clean(self):
        cleaned_data = super(UserEditForm, self).clean()
        password = cleaned_data.get("password")
        password_conf = cleaned_data.get("password_conf")

        if password and password_conf and password != password_conf:
            raise forms.ValidationError(
                "The two password do not match."
            )

    def clean_username(self):
        if self.cleaned_data['username'] == "":
            raise forms.ValidationError("Please insert username.")

        if User.objects.filter(
            email=self.cleaned_data['username']).exclude(
                email=self.instance.username).exists():
            raise forms.ValidationError(("This username already exits."))

        return self.cleaned_data['username']

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
            user.username = user.email
            user.is_active = False
            user.save()
