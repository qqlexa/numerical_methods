from django import forms
from django.forms import ModelForm, CharField, TextInput


class NameForm(forms.Form):
    matrix_size = forms.DecimalField(label='Enter size of matrix', min_value=2, max_value=20,
                                     widget=TextInput(attrs={'type': 'number', 'autocomplete': 'off'}))
