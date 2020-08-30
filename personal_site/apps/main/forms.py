from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(max_length=400, required=True)