import string
import random
from django.core.cache import cache

from api.exceptions import TokenInvalidException


def prepare_cached_value(result_data, uid, scope):
    return dict(uid=uid, scope=scope, **result_data)


def save_to_cache(key, value, expired=7200):
    cache.set(key, value, expired)


def get_current_token_var(token, key):
    result = cache.get(token)
    if not result:
        raise TokenInvalidException
    ret = result.get(key)
    if not ret:
        raise TokenInvalidException('token处理内部错误')
    return result.get(key)


def get_current_uid(token):
    return get_current_token_var(token, 'uid')


def get_random_strings(length=32):
    """
    get a random strings default length is 32.
    :param length: length of strings
    :return: strings
    """
    string_pool = string.ascii_letters + string.digits
    return ''.join(random.sample(string_pool, length))


SUCCESS_MESSAGE = {
    'msg': 'success',
    'error_code': 0,
    'code': 201,
}