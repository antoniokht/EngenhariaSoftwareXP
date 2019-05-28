from django.urls import path
from . import views
from .views import AnswerDeleteView, AnswerUpdateView, AnswerCreateView

urlpatterns = [
    path('answer/new/question/<int:question_id>/',
         AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:pk>/delete/',
         AnswerDeleteView.as_view(), name='answer-delete'),
    path('answer/<int:pk>/update/',
         AnswerUpdateView.as_view(), name='answer-update'),

]
