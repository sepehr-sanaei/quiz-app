from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'op1', 'op2', 'op3', 'op4', 'ans']