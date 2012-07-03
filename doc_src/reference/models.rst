===============
Model Reference
===============

.. contents:: Table of Contents
   :depth:  2
   :local:
   :backlinks: top


ArticleBase
===========

.. py:class:: ArticleBase

   This is the core model and basis for all management. It includes the basic fields.

   .. py:attribute:: title

      **Required** :py:class:`CharField(255)`

      The title or headline of the item.

   .. py:attribute:: subtitle

      :py:class:`CharField(255)`

      An optional subtitle or subheadline for the item.

   .. py:attribute:: slug

      **Required** :py:class:`SlugField`

      URL-friendly title. It is automatically generated from the ``title``.

   .. py:attribute:: summary

      :py:class:`TextField`

      Is this item active. If it is inactive, all children are set to inactive as well.

   .. py:attribute:: content

      **Required** :py:class:`TextField`

      The primary content of the item. The "article" of ``ArticleBase``.

.. _attribution_mixins:

Attribution Mixins
==================

SingleAuthorMixin
-----------------

.. py:class:: SingleAuthorMixin

   A mixin that adds a relation to another model (typically auth.User)

   .. py:attribute:: author

      :py:class:`ForeignKey` ``(`` :py:class:`django.contrib.auth.models.User` ``)``

      The model to which this field relates is set in :ref:`authormodel_setting`. The default is ``auth.User``. You can limit the choices available using the :ref:`authormodellimit_setting` setting.

      In your custom Admin class, you may want to include this field in ``raw_id_fields`` to reduce load time.


MutliAuthorMixin
----------------

.. py:class:: MultiAuthorMixin

   A mixin that adds a many-to-many relation to another model (typically auth.User)

   .. py:attribute:: author

      :py:class:`ManyToManyField` ``(`` :py:class:`django.contrib.auth.models.User` ``)``

      The model to which this field relates is set in :ref:`authormodel_setting`. The default is ``auth.User``. You can limit the choices available using the :ref:`authormodellimit_setting` setting.


NonStaffAuthorMixin
-------------------

.. py:class:: NonStaffAuthorMixin

   A mixin that adds a character field to set a one-time or non-staff author

   .. py:attribute:: author

      :py:class:`CharField(200)`

      An HTML-formatted rendering of an author or authors not on staff.

.. _key_image_mixins:

Key Image Mixins
================

KeyImageMixin
-------------

.. py:class:: KeyImageMixin

   A mixin that allows author's to upload a file to their article. Manages the height and width in fields and provides for a credit to the media's author as well.

   .. py:attribute:: key_image

      :py:class:`ModelUploadFileField`

      A custom Django FileField that uses the name of the model as the default ``upload_to`` location. :ref:`imagestorage_setting` allows for customization of the storage engine and :ref:`imageuploadto_setting` allows customization of the ``upload_to`` path.

   .. py:attribute:: key_image_width

      :py:class:`IntegerField`

      A private field for keeping track of the key image's width. This field is auto-populated when the record is saved.

   .. py:attribute:: key_image_height

      :py:class:`IntegerField`

      A private field for keeping track of the key image's height. This field is auto-populated when the record is saved.

   .. py:attribute:: key_image_credit

      :py:class:`CharField(255)`

      An optional field to store an attribution for the key image, if necessary

.. _publishing_mixins:

Publishing Mixins
=================

Publishing Mixins provide for a workflow, even if it is as simple as "Draft->Finished". With a workflow, only one state is viewable on the site.

PubWorkflowMixin
----------------

This mixin provides for a simple, linear workflow using a choice list. Four settings define crucial aspects to the workflow:


* :ref:`statuschoices_setting` is the ``tuple`` of ``(int, 'choice')`` that defines the key, value pairings.
* :ref:`defaultstatus_setting` is the key for the status choice when you first create an article.
* :ref:`publishedstatus_setting` is the key for the status meaning it is live on the site.
* :ref:`unpublishedstatus_setting` is the key to use when "unpublishing" an item.


.. py:class:: PubWorkflowMixin

   .. py:attribute:: status

      *Required* :py:class:`IntegerField`

      The current state of the article.

   .. py:attribute:: pub_date

      :py:class:`DateField`

      The date in which the article was or will be published. The date and time are separated to provide support for uniqueness by date published. A ``datetime`` value will allow multiple articles with the same slug on the same date, since the published times will likely be different.

   .. py:attribute:: pub_time

      :py:class:`TimeField`

      The time in which the article was or will be published.

   .. py:attribute:: published

      ``boolean property``

      The ``published`` property allows the workflow to act like a boolean. It returns ``True`` if the article's :py:attr:`PubWorkflowMixin.status` equals the :ref:`publishedstatus_setting`.

      If you set this attribute to ``True``, it updates its :py:attr:`PubWorkflowMixin.pub_date` and :py:attr:`PubWorkflowMixin.pub_time` and the :py:attr:`PubWorkflowMixin.status` to :ref:`publishedstatus_setting`.

      If you set this attribute to ``False``, it updates its :py:attr:`PubWorkflowMixin.status` to :ref:`unpublishedstatus_setting`.

   .. py:attribute:: objects

      :py:class:`PubWorkflowManager`

      A subclass of :py:class:`Manager` that adds a :py:meth:`PubWorkflowManager.published` method.

.. py:class:: PubWorkflowManager

   A subclass of Django's default model manager that adds shortcut functions to get published content

   .. py:method:: published

      Returns a :py:class:`QuerySet` of all published content as of the date and time first called.

      :rtype: :py:class:`QuerySet`
