from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=100, default="")
    pub_date = models.DateTimeField(default=datetime.now())
    #datetime.date.today()

    #def __str__(self):
    #    return self.question_text

class Choice(models.Model):
    together = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)