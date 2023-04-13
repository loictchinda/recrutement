from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Utilisateur(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    
    class meta:
        ordering = ['-date_added']
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nom', 'prenom')
        
    def save(self, commit=True):
        user = super(Utilisateur,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user