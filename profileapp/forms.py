from .models import profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput  # Ensure this import is correct
from django import forms

class ProfileForm(ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY', 'class': 'form-control', 'type': 'text'}),
        input_formats=['%Y-%m-%d'],  # Ensure the format is DD/MM/YYYY
        label='Date of Birth'
    )
    class Meta:
        model = profile
        fields = ['name', 'bio', 'profile_pic', 'dob', 'country', 'pincode', 'address']
        widgets = {  # Corrected the typo here
            'profile_pic': FileInput(),  # Add any custom attributes if needed
        }
