from django.urls import path

from . import views, api_views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/<int:pk>', views.IndexDetailView.as_view(), name='question_list'),
    path('polls/<int:pk>/results', views.vote, name='results'),

    # API

    path('login/', api_views.login, name='login'),
    # poll
    path('poll/create/', api_views.poll_create, name='poll_create'),
    path('poll/update/<int:poll_id>/', api_views.poll_update, name='poll_update'),
    path('poll/view/', api_views.polls_view, name='polls_view'),
    path('poll/view/active/', api_views.active_polls_view, name='active_poll_view'),
    # question
    path('question/create/', api_views.question_create, name='question_create'),
    path('question/update/<int:question_id>/', api_views.question_update, name='question_update'),
    # choice
    path('choice/create/', api_views.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', api_views.choice_update, name='choice_update'),
    # answer
    path('answer/create/', api_views.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', api_views.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', api_views.answer_update, name='answer_update'),
]
