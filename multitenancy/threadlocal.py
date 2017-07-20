# Based on
# http://chase-seibert.github.io/blog/2012/06/15/django-ditch-objectsusing-in-favor-of-a-per-view-decorator-to-switch-databases.html

import threading
from functools import wraps


threadlocal = threading.local()


class thread_local(object):
    """ a decorator that wraps a function in a thread local definition block
    useful for passing variables down the stack w/o actually passing them
    examples: what database to read from, whether to cache queries, etc
    adapted from django.test.utils.override_settings

    Usage:

    @thread_local(SITE_NAME_SHORT='foobar')
    def override(request):
        ...

    """

    def __init__(self, **kwargs):
        self.options = kwargs

    def __enter__(self):
        for attr, value in self.options.items():
            setattr(threadlocal, attr, value)

    def __exit__(self, exc_type, exc_value, traceback):
        for attr in self.options.keys():
            setattr(threadlocal, attr, None)

    def __call__(self, test_func):

        @wraps(test_func)
        def inner(*args, **kwargs):
            # the thread_local class is also a context manager
            # which means it will call __enter__ and __exit__
            with self:
                return test_func(*args, **kwargs)

        return inner


def get_thread_local(attr, default=None):
    """ use this method from lower in the stack to get the value """
    return getattr(threadlocal, attr, default)
