import datetime
import os

from django.db.models.fields.files import FileField
from django.core.files.storage import default_storage
from django.utils.encoding import force_unicode, smart_str


class ModelUploadFileField(FileField):
    """
    Makes the upload_to parameter optional by using the name of the model
    """
    def __init__(self, verbose_name=None, name=None, storage=None, **kwargs):
        for arg in ('primary_key', 'unique'):
            if arg in kwargs:
                raise TypeError("'%s' is not a valid argument for %s." % (arg, self.__class__))

        self.storage = storage or default_storage
        upload_to = kwargs.pop('upload_to', '$$MODEL$$')
        if not upload_to:
            upload_to = '$$MODEL$$'
        self.upload_to = upload_to
        if callable(upload_to):
            self.generate_filename = upload_to

        kwargs['max_length'] = kwargs.get('max_length', 100)
        super(FileField, self).__init__(verbose_name, name, **kwargs)

    def get_directory_name(self):
        return os.path.normpath(force_unicode(datetime.datetime.now().strftime(smart_str(self.upload_to))))

    def generate_filename(self, instance, filename):
        if self.upload_to == '$$MODEL$$':
            self.upload_to = instance._meta.verbose_name
        return os.path.join(self.get_directory_name(), self.get_filename(filename))
