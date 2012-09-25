from articleappkit.models import (get_article_base, get_singleauthor_mixin,
                                   get_keyimage_mixin, get_pubworkflow_mixin)

ArticleBase = get_article_base()
SingleAuthorMixin = get_singleauthor_mixin()
KeyImageMixin = get_keyimage_mixin()
PubWorkflowMixin = get_pubworkflow_mixin()


class Story(ArticleBase, SingleAuthorMixin, KeyImageMixin, PubWorkflowMixin):
    """
    Creates a basic story model with a single author, related to auth.User,
    It has a Key Image and contains some useful publishing metadata.
    """
    pass

    class Meta:
        verbose_name_plural = u'stories'