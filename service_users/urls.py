from django.urls import path

from . import views

urlpatterns = [
    # path('otp/generate', views.GenerateOTPView.as_view()),
    path('users', views.ServiceUsersDetailsView.as_view()),
    # path('otp/verify', views.VerifyOTPView.as_view()),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
