from django import forms
from .models import Student_model


class Student_form(forms.ModelForm):
    class Meta:
        model=Student_model
        fields="__all__"