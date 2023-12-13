from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(
        max_length=254,
        widget=forms.PasswordInput()
    )


class RegisterForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=16)
    password = forms.CharField(
        max_length=254,
        widget=forms.PasswordInput()
    )
