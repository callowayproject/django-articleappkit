===============
Model Reference
===============

ModelName
=========

.. py:class:: ModelName

   .. py:attribute:: parent
   
      :py:class:`TreeForeignKey` ``(self)``
   
      The category's parent category. Leave this blank for an root category.

   .. py:attribute:: name
   
      **Required** ``CharField(100)``
   
      The name of the category.

   .. py:attribute:: slug
   
      **Required** ``SlugField``
   
      URL-friendly title. It is automatically generated from the title.

   .. py:attribute:: active
   
      **Required** ``BooleanField`` *default:* ``True``
   
      Is this item active. If it is inactive, all children are set to inactive as well.


ArticleBase
-----------

This is the core model and basis for all management. It includes the basic fields.

* Title. Required. Populates slug.
* Subtitle. Not required
* Slug. Required. Used in URLs
* Summary. Not required.
* Content

Attribution Mixins

   Single author (staff only)
   User is author
   many authors
   write in author

KeyImageMixin

PublishingMixin

