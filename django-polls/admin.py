from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    raw_id_fields = ["question"]
    show_change_link = True

class QuestionAdmin(admin.ModelAdmin):
    show_facets = admin.ShowFacets.NEVER
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information" ,{"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    #save_as = True
    search_help_text = "Поиск по вопросам"

class ChoiceAdmin(admin.ModelAdmin):
    view_on_site = True
    autocomplete_fields = ["question"]
    #raw_id_fields = ["question"]
    list_select_related = ["question"]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
