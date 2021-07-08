from .default import *

ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'common.renderers.EmberJSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'common.errors.custom_exception_handler',
}
