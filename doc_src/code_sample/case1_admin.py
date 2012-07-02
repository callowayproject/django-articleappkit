from django.contrib import admin
from articleappkit.admin import (ArticleBaseAdmin, ARTICLE_BASE_FIELDSET,
                                  SINGLE_AUTHOR_FIELDSET, KEY_IMAGE_FIELDSET,
                                  PUBLISHING_FIELDSET)

from .models import Story


class StoryAdmin(ArticleBaseAdmin):
    fieldsets = (
        ARTICLE_BASE_FIELDSET,
        SINGLE_AUTHOR_FIELDSET,
        KEY_IMAGE_FIELDSET,
        PUBLISHING_FIELDSET,
    )
admin.site.register(Story, StoryAdmin)