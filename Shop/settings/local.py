from .default import *


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'common.renderers.EmberJSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'common.errors.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'common.paging.CustomPageNumberPagination',
    # 'PAGE_SIZE': 1, # có thể bỏ
}

