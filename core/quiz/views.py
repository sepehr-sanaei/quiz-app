from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Quiz
from django.views import View
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)

from .forms import QuizForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Test(LoginRequiredMixin, ListView):
    '''
        a simple view to send questions to html template
    '''
    model = Quiz
    context_object_name = 'question'
    template_name = 'test.html'
    queryset = Quiz.objects.all()
    login_url = "/accounts/access-denied/"




class SubmitQuizView(View):
    def post(self, request, *args, **kwargs):
        answers = dict(request.POST.lists())
        score = 0
        count = Quiz.objects.all().count()
        for question_id, answer in answers.items():
            if question_id == 'csrfmiddlewaretoken':
                continue
            if Quiz.objects.get(id=question_id).ans == answer[0]:
                score += 1
        final_score = (score/count)*100
        return render(request, 'results.html', {'final_score': final_score})
    
    

class CreateQuestionView(CreateView):
    model = Quiz
    template_name = 'test-create.html'
    fields = ('question', 'op1', 'op2', 'op3', 'op4', 'ans')
    
    
    success_url = '/'

class UpdateQuestionView(UpdateView):
    model = Quiz
    template_name = 'test-edit.html'
    form_class = QuizForm
    success_url = '/'
    
    
    
class DeleteQuestionView(DeleteView):
    model = Quiz
    success_url = '/'
    template_name = 'quiz_delete_confirm.html'
    

    
