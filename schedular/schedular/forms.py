from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField()