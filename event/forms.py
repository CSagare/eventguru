from django import forms
from .models import contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacts
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # You can add additional customization here if needed
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 5})
