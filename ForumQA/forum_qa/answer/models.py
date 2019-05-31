from django.db import models
from django.contrib.auth.models import User
from question.models import Question
from django.urls import reverse


class Answer(models.Model):
    content = models.TextField(verbose_name="Resposta")
    # Date posted is automatically set to time when it is posted
    date_posted = models.DateTimeField(auto_now_add=True)
    # When user is deleted, answer is also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # When question is deleted, answer is also deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Number of upvotes and downvotes are initially zero
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.question.pk})

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:20] + " [...]"
        return self.content
