from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_email_verification import sendConfirm
from django.contrib.gis.forms import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists, please try another email.")
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken, please try another one. ")
        return self.cleaned_data


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            sendConfirm(user)

        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.all().exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError("Email already exists, please try another email")
        username = self.cleaned_data.get('username')
        if User.objects.all().exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError("Username already taken, please try another one.")
        return self.cleaned_data