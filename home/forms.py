from django import forms
from .models import Profile, Task
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'image']

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'نام کاربری'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل'
            }),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'نام کاربری'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل'
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'task-title', 'placeholder': 'مثلا مطالعه فصل اول'}),
            'content': forms.Textarea(
                attrs={'id': 'task-description', 'placeholder': 'توضیحات مربوط به این تسک را بنویسید...'})
        }
