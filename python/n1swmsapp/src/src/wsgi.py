"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import time
import traceback
import sys
import signal

from django.core.wsgi import get_wsgi_application

BASE_ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))


sys.path.append(BASE_ROOT_DIRECTORY)
sys.path.append(os.path.join(BASE_ROOT_DIRECTORY, 'environment/lib/python3.8/site-packages'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')


try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(sys.getpid(), signal.SIGINT)
        time.sleep(2.5)
