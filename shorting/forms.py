from django import forms
from .utils import custom_url_validator


class LinkForm(forms.Form):
    url = forms.CharField(label='',
                          widget=forms.TextInput(attrs={'placeholder': 'Your URL here', 'id': 'link-text'})
                          )

    def clean(self):
        cleaned_data = super().clean()
        validation_result = custom_url_validator(cleaned_data.get('url'))
        if not validation_result:
            raise forms.ValidationError('Not an URL! Please enter a valid URL adress')