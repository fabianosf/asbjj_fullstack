from django.urls import path
from .views import HomeView, AboutView, ServiceView, ContactView, LoginView, SignupView
from .views import PasswordResetRequestView, PasswordResetConfirmView


urlpatterns = [
    path('api/home/', HomeView.as_view(), name='home'),
    path('api/about/', AboutView.as_view(), name='about'),
    path('api/service/', ServiceView.as_view(), name='service'),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/password_reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('api/password_reset_confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

