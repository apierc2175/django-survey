from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]
admin.site.register(Question)
# Register your models here.
