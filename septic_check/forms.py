from django import forms


class PropertyForm(forms.Form):
    address = forms.CharField(label='Address', max_length=100)
    zipcode = forms.CharField(label='Zipcode', max_length=10)
