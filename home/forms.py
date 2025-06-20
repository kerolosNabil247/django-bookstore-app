from django.forms import ModelForm
from .models import Books
from django import forms

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
        }