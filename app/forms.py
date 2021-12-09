from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'

