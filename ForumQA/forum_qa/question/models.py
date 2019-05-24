from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name="Descrição breve")
    content = models.TextField(verbose_name="Conteúdo da pergunta")
    # Date posted is automatically set to time when it is posted
    date_posted = models.DateTimeField(auto_now_add=True)
    # When user is deleted, question is also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Number of upvotes and downvotes are initially zero
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})
