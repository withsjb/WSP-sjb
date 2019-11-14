from django.contrib import admin


from django.contrib import admin
from .models import Question, Choice
from . import models

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


