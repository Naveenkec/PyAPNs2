# -*- coding: utf-8 -*-
"""
hyper/common/util
~~~~~~~~~~~~~~~~~

General utility functions for use with hyper.
"""
from enum import Enum

from ..compat import unicode, bytes, imap
from rfc3986 import URIReference
from ..compat import is_py3


def to_bytestring(element):
    """
    Converts a single string to a bytestring, encoding via UTF-8 if needed.
    """
    if isinstance(element, unicode):
        return element.encode('utf-8')
    elif isinstance(element, bytes):
        return element
    else:
        raise ValueError("Non string type.")


def to_bytestring_tuple(*x):
    """
    Converts the given strings to a bytestring if necessary, returning a
    tuple. Uses ``to_bytestring``.
    """
    return tuple(imap(to_bytestring, x))


def to_host_port_tuple(host_port_str, default_port=80):
    """
    Converts the given string containing a host and possibly a port
    to a tuple.
    """
    uri = URIReference(
        scheme=None,
        authority=host_port_str,
        path=None,
        query=None,
        fragment=None
    )

    host = uri.host.strip('[]')
    if not uri.port:
        port = default_port
    else:
        port = int(uri.port)

    return (host, port)


def to_native_string(string, encoding='utf-8'):
    if isinstance(string, str):
        return string

    return string.decode(encoding) if is_py3 else string.encode(encoding)


class HTTPVersion(Enum):
    """
    Collection of all HTTP versions used in hyper.
    """
    http11 = "HTTP/1.1"
    http20 = "HTTP/2"
