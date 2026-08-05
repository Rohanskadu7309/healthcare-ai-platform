from django.urls import path

from .views import RegisterAPIView, LoginAPIView, RefreshTokenAPIView, LogoutAPIView, ProfileAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register",),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh/", RefreshTokenAPIView.as_view(), name="refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path("forgot-password/", ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordAPIView.as_view(), name="reset-password"),
]