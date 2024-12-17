from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['code', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})