import hashlib
import logging
import random
import re

from django.db.utils import IntegrityError

from .exceptions import InvalidDomain, UrlExist, UnknownException
from .models import UrlStorage

logger = logging.getLogger(__name__)


class UrlShorter:

    DOMAIN_PATTERN = r'http[s]?\:\/\/[a-z0-9_\.-]+\.[a-z\.]{1,6}/'
    SHORT_PART_LEN = 10
    RETRY = 5

    def __init__(self, long_url: str, user=None):
        self._long_url = long_url
        self._user = user

    def _get_short_url(self) -> str:
        url_part_to_encode = self._split_url_by_domain()
        short_part_url = self._encode_string(url_part_to_encode)
        return self._get_domain + short_part_url

    def _split_url_by_domain(self) -> str:
        return re.sub(self.DOMAIN_PATTERN, '', self._long_url)

    @property
    def _get_domain(self) -> str:
        domain = re.match(self.DOMAIN_PATTERN, self._long_url)
        if not domain:
            logger.error(f'Invalid domain: {domain}')
            raise InvalidDomain
        return domain.group(0)

    def _encode_string(self, string_to_encode: str) -> str:
        if not string_to_encode:
            return string_to_encode
        string_hash = hashlib.sha256(string_to_encode.encode('utf-8')).hexdigest()
        return ''.join(random.choice(string_hash) for _ in range(self.SHORT_PART_LEN))

    def save_short_url(self) -> UrlStorage:
        short_url = ''
        retry = self.RETRY
        while retry:
            try:
                short_url = self._get_short_url()
                url_storage = UrlStorage.objects.create(
                    owner=self._user,
                    url_long=self._long_url,
                    url_short=short_url,
                )
                return url_storage
            except IntegrityError:
                logger.error(f'Short url {short_url} already exist')
                retry -= 1
                if not retry:
                    raise UrlExist
            except Exception as e:
                logger.error(f"Unknown exception: {e}")
                raise UnknownException
