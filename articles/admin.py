from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_counter = 0

        for form in self.forms:
            if form.cleaned_data.get('is_main', False):
                main_counter += 1

        if main_counter > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
