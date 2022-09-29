from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['date', 'title', 'description']
        widgets = {
            'date' : forms.DateInput(attrs={'class': 'form-control','placeholder': "Pilih tanggal ", "type": "date"}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'})
        }
