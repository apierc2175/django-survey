from django.db import models
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('surveys:index')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
#below returns the string of self.choice_text the [:20] only returns the first 20 characters
    def __str__(self):
        return self.choice_text[:20]
