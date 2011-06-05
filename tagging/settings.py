"""
Convenience module for access of custom tagging application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.
"""
from django.conf import settings

# The maximum length of a tag's name.
MAX_TAG_LENGTH = getattr(settings, 'MAX_TAG_LENGTH', 50)
MAX_TAG_NAMESPACE_LENGTH = getattr(settings, 'MAX_TAG_VALUE_LENGTH', 50)
MAX_TAG_NAME_LENGTH = getattr(settings, 'MAX_TAG_NAME_LENGTH', 50)
MAX_TAG_VALUE_LENGTH = getattr(settings, 'MAX_TAG_VALUE_LENGTH', 50)

# limit the max size attributes to 50 per field, because the model fields
# cannot store longer values.
if MAX_TAG_NAMESPACE_LENGTH is None or MAX_TAG_NAMESPACE_LENGTH > 50:
    MAX_TAG_NAMESPACE_LENGTH = 50
if MAX_TAG_NAME_LENGTH is None or MAX_TAG_NAME_LENGTH > 50:
    MAX_TAG_NAME_LENGTH = 50
if MAX_TAG_VALUE_LENGTH is None or MAX_TAG_VALUE_LENGTH > 50:
    MAX_TAG_VALUE_LENGTH = 50

# Whether to force all tags to lowercase before they are saved to the
# database.
FORCE_LOWERCASE_TAGS = getattr(settings, 'FORCE_LOWERCASE_TAGS', False)
