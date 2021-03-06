
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}



REPLY_PAGE_SIZE = 10
DEBUG = True
TEMPLATE_DEBUG = DEBUG

BACKTYPE_API_KEY = ''

import markdown
from docutils.core import publish_parts

def render_rest(markup):
    parts = publish_parts(source=markup, writer_name="html4css1")
    return parts["fragment"]


from markupfield.markup import DEFAULT_MARKUP_TYPES
from dinette.libs.postmarkup import render_bbcode

DEFAULT_MARKUP_TYPES.append(('bbcode', render_bbcode))
MARKUP_RENDERERS = DEFAULT_MARKUP_TYPES

DEFAULT_MARKUP_TYPE = "markdown"
