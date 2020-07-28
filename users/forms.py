from django import forms
from django.contrib.auth.models import User

from . import models


class RegistrationForm(forms.Form):
    """
    This is the registration form.
    """

    username = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        required=True,
    )

    password_1 = forms.CharField(
        required=True, help_text="Please use a long, unique password."
    )

    password_2 = forms.CharField(required=True, help_text="Repeat your password.")

    def clean_username(self):

        username = self.cleaned_data.get("username")

        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is in use")

    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")

        if not password_2:
            raise forms.ValidationError("You must confirm your password")
        if password_1 != password_2:
            raise forms.ValidationError("Your passwords do not match")
        return password_2


class ProfileForm(forms.ModelForm):
    """
    Form for eidting a profile.
    """

    class Meta:
        model = models.Profile
        fields = ('dark_mode',)
