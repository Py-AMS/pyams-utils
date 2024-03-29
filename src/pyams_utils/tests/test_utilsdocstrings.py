#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""
Generic test case for pyams_utils docstrings
"""

__docformat__ = 'restructuredtext'

import doctest
import os
import unittest

from pyams_utils.tests import get_package_dir


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


def doc_suite(test_dir, globs=None):
    """Returns a test suite, based on doc tests strings found in /*.py"""
    suite = []
    if globs is None:
        globs = globals()

    flags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE |
             doctest.REPORT_ONLY_FIRST_FAILURE)

    package_dir = get_package_dir(test_dir)

    # filtering files on extension
    docs = [doc for doc in
            os.listdir(package_dir) if doc.endswith('.py')]
    docs = [doc for doc in docs if not doc.startswith('__')]

    for test in docs:
        with open(os.path.join(package_dir, test)) as fd:  # pylint: disable=invalid-name
            content = fd.read()
        if '>>> ' not in content:
            continue
        test = test.replace('.py', '')
        location = 'pyams_utils.%s' % test
        suite.append(doctest.DocTestSuite(location, optionflags=flags,
                                          globs=globs))

    return unittest.TestSuite(suite)


def test_suite():
    """returns the test suite"""
    return doc_suite(CURRENT_DIR)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
