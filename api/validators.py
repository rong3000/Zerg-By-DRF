from rest_framework.exceptions import ParseError


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
            raise ParseError(self.message)


