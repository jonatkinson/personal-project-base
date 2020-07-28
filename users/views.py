from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models as user_models
from django.contrib.auth import authenticate, login
from django.urls import reverse

from . import models
from . import forms


def register(request):
    """
    This is the registration process.
    """

    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            # Create the user object.
            user = user_models.User.objects.create_user(
                form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password_1"],
            )
            user.save()

            # Create the user profile.
            profile = models.Profile(user=user)
            profile.save()

            # Log the user in.
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password_1"],
            )
            login(request, user)

            # Or send the user to the homepage.
            return redirect(reverse("home"))
    else:
        form = forms.RegistrationForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request, username):
    """
    This is the profile screen.
    """

    user = get_object_or_404(user_models.User, username=username)
    profile = models.Profile.objects.get(user=request.user)

    if request.method == "POST":
       profile_form = forms.ProfileForm(request.POST, instance=profile)
       if profile_form.is_valid():
           profile_form.save() 
    else:
        profile_form = forms.ProfileForm(instance=profile)    

    return render(request, "users/profile.html", {
        'user': user,
        'profile': profile,
        'form': profile_form,
    })