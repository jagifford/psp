from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Brother, Chapter


MAX_PASSWORD_LENGTH = 30
MIN_PASSWORD_LENGTH = 8
MAX_USERNAME_LENGTH = 50
MIN_USERNAME_LENGTH = 5


class RegistrationForm(forms.Form):
    """
    Form used to register users
    """
    username = forms.CharField(label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    email = forms.CharField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    chapter = forms.ModelChoiceField(label='Chapter', initial='DB', queryset=Chapter.objects.all())

    def clean(self):
        """
        Validates form
        """
        self.verify_password()
        self.verify_username()
        super(RegistrationForm, self).clean()

    def verify_password(self):
        """
        Passwords must match, have at least one numeric and one alpha character,
        and be between 8 and 30 characters long.
        """
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if len(password1) < MIN_PASSWORD_LENGTH:
            raise forms.ValidationError("Password must have at least " + str(MIN_PASSWORD_LENGTH) + " characters")
        elif len(password1) > MAX_PASSWORD_LENGTH:
            raise forms.ValidationError("Password must have less than " + str(MAX_PASSWORD_LENGTH) + " characters")
        elif password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        elif not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must have at least one number")
        elif not any(char.isalpha() for char in password1):
            raise forms.ValidationError("Passwords must have at least one letter")

    def verify_username(self):
        """
        Username must be between 5 and 50 characters long.
        """
        username = self.cleaned_data['username']
        if len(username) < MIN_USERNAME_LENGTH:
            raise forms.ValidationError("Username must have at least " + str(MIN_USERNAME_LENGTH) + " characters")
        elif len(username) > MAX_USERNAME_LENGTH:
            raise forms.ValidationError("Username must have less than " + str(MAX_USERNAME_LENGTH) + " characters")
        elif User.objects.filter(username=username).count():
            """Username already taken"""
            raise forms.ValidationError('Username "%s" is already in use.' % username)

    def register_member(self, request):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        chapter = self.cleaned_data['chapter']

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        Brother(user=user, chapter=chapter, slug=username).save()
        user = authenticate(username=username, password=password)
        login(request, user)


class LoginForm(forms.Form):

    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        """
        Validates form
        """
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is  None:
            raise forms.ValidationError('Username or password incorrect.')
        super(LoginForm, self).clean()

    def login_brother(self, request):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            raise forms.ValidationError('Username or password incorrect.')
