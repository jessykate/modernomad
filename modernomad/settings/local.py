import sys
from .common import *  # noqa
from .common import INSTALLED_APPS, MIDDLEWARE

DEBUG = True
RUNNING_TESTS = 'test' in sys.argv

if not RUNNING_TESTS:
    try:
        import debug_toolbar
        INSTALLED_APPS += [
            'debug_toolbar'
        ]
        MIDDLEWARE = MIDDLEWARE + ('debug_toolbar.middleware.DebugToolbarMiddleware', )

        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': lambda request: True if DEBUG else False,
            'RESULTS_CACHE_SIZE': 100,
        }
    except ImportError:
        print("Django Debug Toolbar Not Installed!")


SECRET_KEY = 'local_development'
