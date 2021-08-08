from django.db import models
from django.db.models.fields import files
from django.forms import fields
from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'