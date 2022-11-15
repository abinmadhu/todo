from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    priority=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Task
        fields='__all__'