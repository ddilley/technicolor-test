
from flask import current_app, flash, redirect, request
from functools import wraps
from urlparse import urlparse
import re

def force_scheme(scheme, permanent=True):
    """
    Forces the given scheme
    """
    def real_decorator(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if current_app.config.get('ENABLE_SCHEME_ENFORCEMENT', True):
                request_scheme = request.headers.get(
                    'X-Forwarded-Proto', urlparse(request.url).scheme)
                if request_scheme.lower() != scheme.lower():
                    return redirect(
                        re.sub('^[A-z]+://', scheme+'://', request.url),
                        302 if not permanent else 301)
            return fn(*args, **kwargs)
        return decorator
    return real_decorator
