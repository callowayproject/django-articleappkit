from articleappkit.models import (get_articlebase, get_singleauthormixin,
                                   get_keyimagemixin, get_pubworkflowmixin)

ArticleBase = get_articlebase()
SingleAuthorMixin = get_singleauthormixin()
KeyImageMixin = get_keyimagemixin()
PubWorkflowMixin = get_pubworkflowmixin()


class Story(ArticleBase, SingleAuthorMixin, KeyImageMixin, PubWorkflowMixin):
    """
    Creates a basic story model with a single author, related to auth.User,
    It has a Key Image and contains some useful publishing metadata.
    """
    pass

    class Meta:
        verbose_name_plural = u'stories'