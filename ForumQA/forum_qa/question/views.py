from django.shortcuts import render

# Temporary:
posts = [
    {
        'author': 'Tomas',
        'title': 'My first question',
        'content': 'How much is...?',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Elisa',
        'title': 'Elisas first question',
        'content': 'Where is...?',
        'date_posted': 'April 3, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'question/home.html', context)


def about(request):
    return render(request, 'question/about.html', {'title': 'About'})
