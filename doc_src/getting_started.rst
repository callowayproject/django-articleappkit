===============
Getting Started
===============


Installation
============

Installation is easy using ``pip`` or ``easy_install``.

.. code-block:: bash

    pip install django-articleappkit



Simple Case
===========

Article App Kit consists of abstract model factories. The model factory allows you to pass a configuration dictionary to set up each class. Django Article App Kit wasn't meant to work by itself. So you will create a brand new app. We'll call this app ``Story``.

**models.py**

.. literalinclude:: code_sample/case1_models.py

In this simple case, we aren't going to change any of the defaults. After we import several model factories, we call them to retrieve the classes. The ``Story`` class inherits from these classes, and nothing else is required except providing a proper ``verbose_name``.

**admin.py**

.. literalinclude:: code_sample/case1_admin.py

**urls.py**

.. literalinclude:: code_sample/case1_urls.py

Modifying field names
=====================

You can override the default field names by adding a ``FIELDNAMES`` key to the ``ARTICLEAPPKIT_SETTINGS`` dictionary. Each key in the ``FIELDNAMES`` dictionary is the existing field name and the value is the new verbose name.

.. code-block:: python

    ARTICLEAPPKIT_SETTINGS = {
        'FIELDNAMES': {
            'title': 'headline',
            'key_image': 'primary image',
            'key_image_credit': 'primary image credit',
        }
    }


Making your own settings
========================

This may have to be a v2 feature. The import logic is wonky as the model needs to import the settings in the module, and the final app imports the classes from the module.

Might try using a metaclass to allow importation of the settings by setting the settings module in the class like:

from storyapp import settings as story_settings

class Story():
    settings = story_settings
    __metaclass__ = ArticleBase


Adding WYSIWYG editors
======================

Adding object relations
=======================