========
Settings
========

FIELDNAMES (a dict mapping the key (original field name) to the new field name) Used as the verbose name of the model and doesn't change the database name or the name developers must use.

AUTHOR_MODEL (app.model to relate authors)

AUTHOR_MODEL_LIMIT (limit_choices_to attribute)

IMAGE_STORAGE

UNIQUE_TOGETHER (with which field is must the slug be unique. Could be publish_date for date-base url schemes. If blank (default) slugs must always be unique)
