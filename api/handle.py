from __future__ import unicode_literals

import six
from django.utils.translation import ugettext_lazy as _

from django.http import Http404
from api.exceptions import *
from rest_framework.compat import set_rollback
from rest_framework.response import Response


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    request_url = context['request'].build_absolute_uri()

    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {
                'msg': exc.detail,
                'code': exc.code,
                'error_code': exc.error_code,
                'request_url': request_url
            }

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

    # else:
    #     msg = '服务器内部错误, 不想告诉你'
    #     data = {
    #         'msg': msg,
    #         'error_code': 999,
    #         'code': 500,
    #         'request_url': request_url
    #     }
    #     set_rollback()
    #     return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


