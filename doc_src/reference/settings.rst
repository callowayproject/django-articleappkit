========
Settings
========

.. contents:: Table of Contents
   :depth:  1
   :local:
   :backlinks: top


Default Settings
================

.. code-block:: python

    ARTICLEAPPKIT_SETTINGS = {
        'FIELDNAMES': {},
        'UNIQUE_TOGETHER': (),
        'AUTHOR_MODEL': 'auth.User',
        'AUTHOR_MODEL_LIMIT': {'is_staff': True},
        'IMAGE_STORAGE': settings.DEFAULT_FILE_STORAGE,
        'IMAGE_UPLOAD_TO': '',
        'STATUS_CHOICES': (
            (0, u'DRAFT'),
            (1, u'PUBLISHED'),
            (2, u'UN-PUBLISHED'),
        ),
        'DEFAULT_STATUS': 0,
        'PUBLISHED_STATUS': 1,
        'UNPUBLISHED_STATUS': 2,
    }

.. _fieldnames_setting:

FIELDNAMES
==========

A ``dict`` mapping the original field name to the new field name. The model uses This value as the verbose name of the model and doesn't change the database name or the name developers must use.

You *must* include the underscores in the key, but *should not* include them in the value.

**Default:** ``{}``

.. _authormodel_setting:

AUTHOR_MODEL
============

The model used for relations in several :ref:`attribution_mixins`. The string should be in ``'app.Model'`` format.

**Default:** ``'auth.User'``

.. _authormodellimit_setting:

AUTHOR_MODEL_LIMIT
==================

A ``dict`` passed to the ``limit_choices_to`` parameter of several :ref:`attribution_mixins`.

**Default:** ``{'is_staff': True}``

.. _imagestorage_setting:

IMAGE_STORAGE
=============

The Django storage engine to use to store images when using :ref:`key_image_mixins`.

**Default:** ``django.conf.settings.DEFAULT_FILE_STORAGE``

.. _imageuploadto_setting:

IMAGE_UPLOAD_TO
===============

A string which is prefixed to the file name when using :ref:`key_image_mixins`. By default, a blank string will use the name of the model.

**Default:** ``''``

.. _uniquetogether_setting:

UNIQUE_TOGETHER
===============

Meant specifically for :py:attr:`ArticleBase.slug` to define its uniqueness. If using one of the :ref:`publishing_mixins`, you might define ``UNIQUE_TOGETHER`` as ``('pub_date', 'slug')`` to make the slug unique by date for date-based url schemes.
If blank (default) slugs must always be unique.

**Default:** ``''``

.. _statuschoices_setting:

STATUS_CHOICES
==============

A tuple of int, string tuples defining the choices for the status field in the :py:class:`PubWorkflowMixin` mixin.

Default: ::

    (
        (0, u'DRAFT'),
        (1, u'PUBLISHED'),
        (2, u'UN-PUBLISHED'),
    )

.. _defaultstatus_setting:

DEFAULT_STATUS
==============

The key of the default status to use in the status field in the :py:class:`PubWorkflowMixin` mixin.

Default: ``0``

.. _publishedstatus_setting:

PUBLISHED_STATUS
================

The key of the status that means the article is available on the site.

Default: ``1``

.. _unpublishedstatus_setting:

UNPUBLISHED_STATUS
==================

The key of the status to use when moving from a published state, to an unpublished state.

Default: ``2``