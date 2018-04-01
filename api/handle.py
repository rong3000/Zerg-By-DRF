from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.http import Http404
from rest_framework.exceptions import *
from rest_framework import exceptions
from rest_framework.compat import set_rollback
from rest_framework.response import Response

from api.models import Banner


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    request_url = context['request'].build_absolute_uri()
    if isinstance(exc, ParseError):
        msg = exc.detail
        data = {
            'msg': msg,
            'code': exc.status_code,
            'error_code': 40000,
            'request_url': request_url
        }
        set_rollback()
        return Response(data, status=exc.status_code)

    elif isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'msg': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {
            'msg': six.text_type(msg),
            'error_code': 40000,
            'request_url': request_url
        }

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'msg': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    else:
        msg = _('Internal server error')
        data = {
            'msg': msg,
            'error_code': 999,
            'request_url': request_url
        }

        set_rollback()
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
