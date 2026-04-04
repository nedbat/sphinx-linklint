.. This is stuff that our test data references, so we need to include it during
    testing to prevent warnings.

    It's important to ensure that this file itself has no excessive links, or
    it will pollute the totals during tests. The simplest way to do that is to
    have no references in this file.

Built-in types
==============

.. class:: bool(object=False, /)

   Return a Boolean value, i.e. one of ``True`` or ``False``.

.. class:: bytearray(source=b'')
           bytearray(source, encoding, errors='strict')

   There is no dedicated literal syntax for bytearray objects, instead
   they are always created by calling the constructor:

.. class:: bytes(source=b'')
           bytes(source, encoding, errors='strict')

   Firstly, the syntax for bytes literals is largely the same as that for string
   literals, except that a ``b`` prefix is added:

.. class:: dict(**kwargs)
           dict(mapping, /, **kwargs)
           dict(iterable, /, **kwargs)

   Return a new dictionary initialized from an optional positional argument
   and a possibly empty set of keyword arguments.

.. class:: float(number=0.0, /)
           float(string, /)

   Return a floating-point number constructed from a number or a string.

.. class:: frozendict(**kwargs)
           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)

   Return a new frozen dictionary initialized from an optional positional
   argument and a possibly empty set of keyword arguments.

.. class:: int(number=0, /)
           int(string, /, base=10)

   Return an integer object constructed from a number or a string, or return
   ``0`` if no arguments are given.

.. class:: list(iterable=(), /)

   Lists may be constructed in several ways:

.. class:: memoryview(object)

   Create a memoryview that references *object*.  *object* must
   support the buffer protocol.

.. class:: range(stop, /)
           range(start, stop, step=1, /)

   The arguments to the range constructor must be integers (either built-in
   int or any object that implements the __index__ special method).

.. class:: set(iterable=(), /)
           frozenset(iterable=(), /)

   Return a new set or frozenset object whose elements are taken from
   *iterable*.

.. class:: str(*, encoding='utf-8', errors='strict')
           str(object)
           str(object, encoding, errors='strict')
           str(object, *, errors)

   Return a string version of *object*.  If *object* is not
   provided, returns the empty string.  Otherwise, the behavior of ``str()``
   depends on whether *encoding* or *errors* is given, as follows.

.. class:: tuple(iterable=(), /)

   Tuples may be constructed in a number of ways:


Glossary
========

.. glossary::

   bytes-like object
      things that are like bytes

   file object
      blah blah

   path-like object
      you know, like a file.


Some keywords
=============

.. _with:

The :keyword:`!with` statement
------------------------------

It uses context managers.
