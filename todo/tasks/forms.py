from django import forms
from django.core.exceptions import ValidationError
from .models import ToDoList, Task


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'List Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List Description'}),
        }

# Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        completed = cleaned_data.get('completed')
        status = cleaned_data.get('status')

        if completed and status != 'Completed':
            cleaned_data['status'] = 'Completed'
        
        if not completed and status == 'Completed':
            raise ValidationError("You cannot mark status as 'Completed' without checking the 'Completed' checkbox.")
        
        return cleaned_data