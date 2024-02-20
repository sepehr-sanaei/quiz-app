from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Quiz

# Create your views here.

class Test(TemplateView):
    '''
        a simple view to send questions to html template
    '''
    model = Quiz
    template_name = 'test.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Quiz.objects.all()
        for quiz in context['question']:
            print(quiz.op1, quiz.op2, quiz.op3, quiz.op4)
        return context