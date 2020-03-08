from django import forms

class NameForm(forms.Form):
    account = forms.CharField(label='account', max_length=100)
