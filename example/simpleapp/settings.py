from django.conf import settings

DEFAULT_SETTINGS = {
    'AUTHOR_MODEL': 'simpleapp.StaffMember',
    'AUTHOR_MODEL_LIMIT': {'is_active': True},
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'SIMPLEAPP_SETTINGS', {}))

globals().update(USER_SETTINGS)