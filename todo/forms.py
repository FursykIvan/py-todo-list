from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags", "done")
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Task content"}),
            "deadline": forms.DateInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "tags": forms.Textarea(attrs={"class": "form-control"}),
            "done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
