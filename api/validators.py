from api.exceptions import ParameterException


class IdsValidator(object):
    message = "请求参数错误，请确认id为正整数且id间用英文','分开"

    def __init__(self, message=None):
        self.message = message or self.message

    @staticmethod
    def _check_ids(value):
        ids = value.split(',')
        if not ids:
            return "id必须用','分割"
        if not all(i.isdigit() for i in ids):
            return 'id必须为正整数'

    def __call__(self, value):
        message = self._check_ids(value)
        if message:
            raise ParameterException(detail=message)


class CountValidator(object):
    message = "请求参数错误，请确认count为正整数"

    def __init__(self, message=None):
        self.message = message or self.message

    def _check_count(self, value):
        if not str(value).isdigit():
            return self.message
        else:
            value = int(value)
            if not 0 < value <= 15:
                return 'count不为0且不超过15'

    def __call__(self, value):
        message = self._check_count(value)
        if message:
            raise ParameterException(message)
        return int(value)
