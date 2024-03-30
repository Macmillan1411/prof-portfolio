# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Full name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}))
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    phone = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(123) 456-7890'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'style': 'height: 10rem;'}))
