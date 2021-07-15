from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)  # This is a tuple, add comma after
        

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'completed')
        # exclude = ('created_date',)
