from blog.views import *
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('test/', test),
    path('accueil/', record),
    path('enreg/', record2),
    path('recherche/', find),
    path('modifier/', rename),
    path('supprimer/', clean),
    path('login_user/',login_user),
    path('register_user', register_user),
    path('logout_user/', logout_user),
    path('config_user/', config_user),
    path('histogramme/', histogramme),
    path('password_reset/', auth_view.PasswordResetView.as_view(), name = "reset_password"),
    path('password_reset_sent/', auth_view.PasswordResetDoneView.as_view(),  name = "password_reset_done"),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(),name = "password_reset_confirm"),
    path('password_complete/', auth_view.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),
]