"""
WSGI config for system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import traceback
import signal
import sys
import time

from django.core.wsgi import get_wsgi_application

BASE_ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))

sys.path.append(BASE_ROOT_DIRECTORY)
sys.path.append(os.path.join(BASE_ROOT_DIRECTORY, 'environment/lib/python3.8/site-packanges'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')

try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
