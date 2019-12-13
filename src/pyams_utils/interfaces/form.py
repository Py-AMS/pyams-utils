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

"""PyAMS_utils.interfaces.form module

This module contains a few special values which are used into forms.
"""

__docformat__ = 'restructuredtext'


class NOT_CHANGED:  # pylint: disable=invalid-name
    """Marker value for unchanged properties"""
    def __repr__(self):
        return '<NOT_CHANGED>'


NOT_CHANGED = NOT_CHANGED()


class NO_VALUE:  # pylint: disable=invalid-name
    """Marker value for properties without value"""
    def __repr__(self):
        return '<NO_VALUE>'


NO_VALUE = NO_VALUE()


class TO_BE_DELETED:  # pylint: disable=invalid-name
    """Marker value for properties to be deleted"""
    def __repr__(self):
        return '<TO_BE_DELETED>'


TO_BE_DELETED = TO_BE_DELETED()
