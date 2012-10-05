from django.contrib import admin
from django.db import models
from django import forms

ARTICLE_BASE_FIELDSET = (
    None, {
        'fields': ('title', 'slug', 'subtitle', 'summary', 'content', 'update_date', )
    }
)

ARTICLE_CONTENT_FIELDSET = (
    None, {
        'fields': ('title', 'subtitle', 'summary', 'content', )
    }
)

ARTCILE_METADATA_FIELDSET = (
    'Metadata', {
        'fields': ('slug', 'create_date', 'update_date', 'modified_date', ),
        'classes': ('collapse', )
    }
)

SINGLE_AUTHOR_FIELDSET = (
    'Author', {
        'fields': ('author', ),
    }
)

MULTI_AUTHOR_FIELDSET = (
    'Authors', {
        'fields': ('authors', ),
    }
)
NONSTAFF_AUTHOR_FIELDSET = (
    'Author', {
        'fields': ('non_staff_author', ),
    }
)

KEY_IMAGE_FIELDSET = (
    'Key Image', {
        'fields': ('key_image', 'key_image_credit', )
    }
)
PUBLISHING_FIELDSET = (
    'Publishing', {
        'fields': ('status', ('pub_date', 'pub_time'), )
    }
)


class ArticleBaseAdmin(admin.ModelAdmin):
    search_fields = ('title', 'subtitle', )
    prepopulated_fields = {'slug': ('title', )}
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': '117'})},
    }
