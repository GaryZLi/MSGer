from django import forms

class LoginForm(forms.Form):
    post = forms.CharField()
    # login_password = forms.CharField(label='login password')