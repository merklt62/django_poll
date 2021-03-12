from django.contrib import admin

from .models import Question, Choice, Poll


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['date_start']
        return self.readonly_fields

    fieldsets = [
        (None, {'fields': ['poll_name']}),
        (None, {'fields': ['date_start']}),
        (None, {'fields': ['date_end']}),
        (None, {'fields': ['description']}),
    ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll']}),
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['question_type']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
