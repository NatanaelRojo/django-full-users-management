from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

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
    # 1. Autenticación personalizada (Login / Logout / Signup)
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    # 2. Vistas de recuperación de contraseña (Sobrescritas para manejar el app_name)
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            html_email_template_name="registration/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_change",
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy("users:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("users:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # 3. Vistas CRUD de usuarios
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
