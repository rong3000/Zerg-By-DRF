import hashlib

from Zerg import settings
from api.utils import get_random_strings
import time


class Token:

    @staticmethod
    def generate_token():
        random_strings = get_random_strings(length=32)
        timestamp = str(time.time())
        salt = settings.SECRET_KEY
        md5 = hashlib.md5()
        md5.update((random_strings + timestamp + salt).encode())
        return md5.hexdigest()
