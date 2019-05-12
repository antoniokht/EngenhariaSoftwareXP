from django.urls import path
from . import views


urlpatterns = [
    path('',  views.home, name='question-home'),
    path('about/',  views.about, name='question-about')
]
