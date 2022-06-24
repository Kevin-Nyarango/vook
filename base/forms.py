from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].label = ''
            new_data = {
                "placeholder": f'{str(field)}',
                "class": 'showcase-form-input'
            }
            self.fields[str(field)].widget.attrs.update(
                new_data)

        self.fields['message'].widget.attrs.update(
            {'class': 'showcase-form-input-row-3 '})
        self.fields['message'].widget.attrs.update(
            {'placeholder': 'Write A Message...'})

