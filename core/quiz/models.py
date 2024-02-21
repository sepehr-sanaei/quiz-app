from django.db import models
from django.urls import reverse
# Create your models here.

class Quiz(models.Model):
    '''
    This is a model for creating quiz questions with 4 choices
    '''
    question = models.TextField(null=True)
    op1 = models.CharField(max_length=255, null=True)
    op2 = models.CharField(max_length=255, null=True)
    op3 = models.CharField(max_length=255, null=True)
    op4 = models.CharField(max_length=255, null=True)
    ans = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.question
    
    
    
