
==================
PyAMS ZODB helpers
==================

PyAMS_utils provides a few helpers to manage ZODB connections.

    >>> import pprint

    >>> from pyramid.testing import setUp, tearDown
    >>> config = setUp()
    >>> config.registry.settings['zodbconn.uri'] = 'memory://'

    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)


Persistent connection adapter
-----------------------------

This adapter provides an adapter to any persistent object:

    >>> from ZODB.interfaces import IConnection
    >>> from transaction.interfaces import ITransactionManager
    >>> from pyams_utils.zodb import ZODBConnection
    >>> conn = ZODBConnection()
    >>> conn
    <pyams_utils.zodb.ZODBConnection object at 0x...>

    >>> with conn as root:
    ...     pprint.pprint((root, IConnection(root), conn.connection, conn.db, conn.storage))
    ({},
     <Connection at ...>,
     <Connection at ...>,
     <ZODB.DB.DB object at 0x...>,
     <ZODB.MappingStorage.MappingStorage object at 0x...>)

    >>> with conn as root:
    ...     pprint.pprint(ITransactionManager(root))
    <transaction._manager.TransactionManager object at 0x...>


ZODB connections vocabulary
---------------------------

A vocabulary of available ZODB connections is available:

    >>> from zope.interface import implementer, Interface
    >>> from zope.schema import Choice
    >>> from pyams_utils.interfaces import ZODB_CONNECTIONS_VOCABULARY_NAME

    >>> class IMyContent(Interface):
    ...     zodb = Choice(title='ZODB connection',
    ...                   vocabulary=ZODB_CONNECTIONS_VOCABULARY_NAME)

    >>> from persistent import Persistent
    >>> from zope.schema.fieldproperty import FieldProperty
    >>> @implementer(IMyContent)
    ... class MyContent(Persistent):
    ...     zodb = FieldProperty(IMyContent['zodb'])

    >>> content = MyContent()
    >>> content.zodb = ''
    >>> content.zodb
    ''
    >>> content.zodb = 'missing'
    Traceback (most recent call last):
    ...
    zope.schema._bootstrapinterfaces.ConstraintNotSatisfied: ('missing', 'zodb')


Using volatile properties
-------------------------

Volatile properties are using volatile attributes of persistent object to save data which
is not stored into ZODB:

    >>> from pyams_utils.zodb import volatile_property
    >>> class MyContent(Persistent):
    ...     @volatile_property
    ...     def value(self):
    ...         pprint.pprint("Getting value...")
    ...         return 1

    >>> content = MyContent()
    >>> content.value
    'Getting value...'
    1

Calling property another time just returns value of volatile attribute:

    >>> content.value
    1

If you delete a volatile property, it's matching attribute is removed:

    >>> del content.value
    >>> content.value
    'Getting value...'
    1


Tests cleanup:

    >>> tearDown()
