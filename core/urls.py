from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views

from users import views as users_views

urlpatterns = [

    # Admin interface.
    path("admin/", admin.site.urls),
        
    # Authentication.
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("register/", users_views.register, name="register"),

    # Profiles.
    path("profile/<str:username>/", users_views.profile, name="profile"),

    # Homepage.
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
