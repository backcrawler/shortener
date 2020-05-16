import string
import random
import re

SOURCE = string.ascii_lowercase + string.digits
HOSTNAME = 'http://localhost:8000'


def short_url_generator(size=7):
    shortcode = ''.join( random.choice(SOURCE) for _ in range(size) )
    return shortcode


PATTERN = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def custom_url_validator(url):
    if re.match(PATTERN, url) is not None:
        return True
    return False