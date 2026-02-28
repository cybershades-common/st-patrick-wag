from django_recaptcha.fields import ReCaptchaField
from django import forms

from contact.models import ContactSubmission
from datetime import datetime


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactSubmission
        fields = ['name', 'email','phone','enquiry','message']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '%s' % self.fields[field].label
