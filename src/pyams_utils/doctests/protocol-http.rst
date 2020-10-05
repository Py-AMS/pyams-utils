
===========================
PyAMS HTTP protocol helpers
===========================

PyAMS provides a few helpers to handle HTTP protocol, and mainly to handle HTTP proxies:

    >>> from pyams_utils.protocol.http import get_client, get_client_from_url

    >>> client = get_client('GET', 'http', 'localhost:18081', '/', {'query': 1})
    >>> client.get_response()
    Traceback (most recent call last):
    ...
    ConnectionRefusedError: [Errno 111] Connection refused

    >>> from unittest.mock import patch
    >>> client = get_client_from_url('http://localhost/',
    ...                              credentials=('login', 'password'),
    ...                              proxy=('localhost', 18081),
    ...                              proxy_auth=('proxy_user', 'proxy_password'))
    >>> with patch('httplib2.Http.request', return_value=(200, 'OK')):
    ...     client.get_response()
    (200, 'OK')
