class InvalidDomain(Exception):
    """Domain is not invalid"""


class UrlExist(Exception):
    """Short url {short_url} already exist"""


class UnknownException(Exception):
    """Unknown exception"""
