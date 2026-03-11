from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views
from django.urls import include, path

from apps.users import views
from apps.users.views import (
    SignUpView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)

app_name = "users"

urlpatterns = [
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            html_email_template_name="registration/password_reset_email.html"
        ),
        name="password_reset",
    ),
    path("", include(auth_urls)),
    path("signup/", SignUpView.as_view(), name="signup"),
    # URLs de autenticación
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # Urls CRUD de usuarios
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
