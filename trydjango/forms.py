from django import forms
from .models import singup

class Contact_form(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clear_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        #if not domain == "USC":
        #    raise forms.ValidationError("Please make sure you use USC email.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address.")
        return email

class sing_up_form(forms.ModelForm):
    class Meta:
        model = singup
        fields = {'full_name', 'email'}
        #exclude = ['full_name', 'email', 'zip_code']

    def clear_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        #if not domain == "USC":
        #    raise forms.ValidationError("Please make sure you use USC email.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address.")
        return email

    def clear_full_name(self):
        full_name =self.cleaned_data.get('full_name')
        return full_name

