import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Poll(models.Model):

    poll_name = models.CharField('название опроса', max_length=200)
    date_start = models.DateTimeField('начало')
    date_end = models.DateTimeField('окончание')
    description = models.TextField('Описание')

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    TEXT = 'text'
    ONCE = 'radio'
    MULTI = 'checkbox'

    choices = (
        (TEXT, 'Text'),
        (ONCE, 'radiobutton'),
        (MULTI, 'checkbox'),
    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,
                             null=True, blank=True)
    question_text = models.CharField(max_length=200,
                                     verbose_name='название вопроса')
    question_type = models.CharField(max_length=20, verbose_name='тип вопроса',
                                     choices=choices, default=TEXT)

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                        null=True, blank=True)
    choice_text = models.CharField(max_length=200,
                                   verbose_name='Вариант ответа')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
