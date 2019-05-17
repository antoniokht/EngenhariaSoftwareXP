from django.shortcuts import render
from .models import Question


def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'question/home.html', context)


def about(request):
    return render(request, 'question/about.html', {'title': 'About'})
