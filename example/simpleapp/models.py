from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField

from articleappkit.models import (get_article_base, get_singleauthor_mixin,
                                   get_keyimage_mixin, get_pubworkflow_mixin)

from .settings import USER_SETTINGS

ArticleBase = get_article_base(USER_SETTINGS)
SingleAuthorMixin = get_singleauthor_mixin(USER_SETTINGS)
KeyImageMixin = get_keyimage_mixin(USER_SETTINGS)
PubWorkflowMixin = get_pubworkflow_mixin(USER_SETTINGS)


class StaffMember(models.Model):
    """
    A User that works for the organization.
    """
    user = models.ForeignKey(User,
        limit_choices_to={'is_active': True},
        unique=True)
    slug = models.SlugField(unique=True)
    bio = models.TextField('Biography', blank=True)
    is_active = models.BooleanField('is a current employee', default=True)
    phone = PhoneNumberField('Phone Number', blank=True)
    photo = models.FileField('Photo',
        blank=True,
        upload_to='img/staff/%Y')


class Story(ArticleBase, SingleAuthorMixin, KeyImageMixin, PubWorkflowMixin):
    """
    Creates a basic story model with a single author, related to auth.User,
    It has a Key Image and contains some useful publishing metadata.
    """
    objects = PubWorkflowMixin.objects

    class Meta:
        verbose_name_plural = u'stories'
