# File to auto-gen forms
from django import forms


class CreateList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)  # complete/incomplete
