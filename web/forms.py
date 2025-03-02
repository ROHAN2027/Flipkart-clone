from django import forms

class HelloForm(forms.Form):
    username = forms.CharField(max_length=100 ,label="Name:", required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=100 ,widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class signupform(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label="Email", required=True)

class marksheet(forms.Form):
    subject1 = forms.FloatField(required=True)
    subject2 = forms.FloatField(required=True)
    subject3 = forms.FloatField(required=True)
    subject4 = forms.FloatField(required=True)
    subject5 = forms.FloatField(required=True)

    