from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Poll


class IndexView(generic.ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls_list'

    def get_queryset(self):
        return Poll.objects.order_by('id')


class IndexDetailView(generic.DetailView):

    model = Poll
    template_name = 'polls/polls_detail.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.all()


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
    context_object_name = 'res'

    def get_queryset(self):
        return Poll.objects.all()

