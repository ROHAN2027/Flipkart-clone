from django import forms
from .models import info

class InfoForm(forms.ModelForm):
    class Meta:
        model = info
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-size: 16px;'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-size: 16px;'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here...', 'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-size: 16px;'}),
        }
