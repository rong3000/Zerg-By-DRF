"""
Handled exceptions raised by REST framework.

In addition Django's built in 403 and 404 exceptions are handled.
(`django.http.Http404` and `django.core.exceptions.PermissionDenied`)
"""
from __future__ import unicode_literals

from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework import status


class APIException(Exception):
    """
    Base class for REST framework exceptions.
    Subclasses should provide `.status_code` and `.default_detail` properties.
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('A server error occurred.')
    default_error_code = 999

    def __init__(self, detail=None, error_code=None, code=None):
        if detail is not None:
            self.detail = force_text(detail)
        else:
            self.detail = force_text(self.default_detail)
        self.error_code = error_code or self.default_error_code
        self.code = code or self.status_code

    def __str__(self):
        return self.detail


class BannerDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '指定横幅不存在，请检查参数'
    default_error_code = 40000


class CategoryDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '指定的类别不存在，请检查参数'
    default_error_code = 50000


class OrderDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '指定的订单不存在，请检查参数'
    default_error_code = 80000


class ThemeDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '指定的专题不存在，请检查参数'
    default_error_code = 30000


class ProductDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '指定的商品不存在，请检查参数'
    default_error_code = 20000


class ForbiddenException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = '权限不够'
    default_error_code = 10001


class TokenInvalidException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Token已过期或无效Token'
    default_error_code = 10001


class ParameterException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '请求参数错误'
    default_error_code = 10000


class WeChatException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '微信服务器接口调用失败'
    default_error_code = 999


class UserException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = '用户不存在，请检查参数'
    default_error_code = 60000
