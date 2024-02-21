from django.contrib import admin
from django.urls import path, include
from .import views

app_name = "quiz"

urlpatterns = [
    path('', views.Test.as_view(), name='test'),
    path('submit_quiz/', views.SubmitQuizView.as_view(), name='submit_quiz'),
    path('create-test/', views.CreateQuestionView.as_view(), name='create-test'),
    path('edit-test/<int:pk>/', views.UpdateQuestionView.as_view(), name='edit-test'),
    path('delete-test/<int:pk>/', views.DeleteQuestionView.as_view(), name='delete-test'),
]