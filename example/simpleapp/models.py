from articleappkit.models import (ArticleBase, SingleAuthorMixin,
                                   KeyImageMixin, PubWorkflowMixin)


class Story(ArticleBase, SingleAuthorMixin, KeyImageMixin, PubWorkflowMixin):
    """
    Creates a basic story model with a single author, related to auth.User,
    It has a Key Image and contains some useful publishing metadata.
    """
    pass

    class Meta:
        verbose_name_plural = u'stories'
