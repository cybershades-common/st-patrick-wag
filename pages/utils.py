from django import forms

def is_email_valid(email):
    f = forms.EmailField()
    email_valid = False
    try:
        f.clean(email)
        email_valid = True
    except forms.ValidationError:
        pass
    return email_valid