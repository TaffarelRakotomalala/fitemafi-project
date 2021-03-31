#coding : utf-8
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormMembres(ModelForm):
    class Meta:
        model = Membres
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nom"].widget.attrs['placeholder'] = "Entrer le nom du membre"
        self.fields["prenoms"].widget.attrs['placeholder'] = "Entrer le prénom du membre"

class FormDroit(ModelForm):
    class Meta:
        model = Droit
        fields = ['droit_adhension', 'droit_annuel', 'droit_reception', 'id_membres']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Entrer votre nom d'utilisateur", 'class': 'test'}), 
            'last_name': forms.TextInput(attrs={'placeholder' : "Entrer votre Nom"}),
            'first_name': forms.TextInput(attrs={'placeholder' : "Entrer votre Prénom"}),
            'email': forms.EmailInput(attrs={'placeholder' : "Entrer votre email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs['placeholder'] = "Entrer Votre mot de passe"
        self.fields["password2"].widget.attrs['placeholder'] = 'Confirmer votre mot de passe'

class EditUserForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['avatar',]

        