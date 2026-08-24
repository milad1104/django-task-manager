from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()

        username = cd.get('username')
        password = cd.get('password')

        if not username or not password:
            raise forms.ValidationError("Please enter both username and password")

        user = User.objects.filter(username=username).first()

        if user is None:
            user = User.objects.create_user(username=username,password=password)
        else:
            user = authenticate(username=username,password=password)

            if user is None:
                raise forms.ValidationError(
                    "Username or password is incorrect"
                )

        cd['user'] = user

        return cd
