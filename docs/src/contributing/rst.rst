==========
RST Syntax
==========

Core Concepts
-------------

You'll find literature on these concepts at :doc:`../literature`

* :ref:`section header <subsection>`
* :ref:`directive <directive>`
* :ref:`role <role>`
* :ref:`reference  <role>`
* :ref:`inline external link <inline_ext_link>`
* :ref:`cross-references <cross_reference>`
* :ref:`root document <root>`
* :ref:`code-block <code>`
* :ref:`domain <domain>`
* :ref:`include .rst file <include_rst_file>`

.. _include_rst_file:
.. _inline_ext_link:

.. _root:

this is the root document

.. _domain:

Domain
------

`read the docs <https://www.sphinx-doc.org/en/master/glossary.html#term-domain>`_

.. _subsection:

Subsection header
--------------

This is a subsection header.

.. _code:

Code block
----------

.. code:: bash

    echo "this is a code block"

.. code-block:: json

    {
        "this": "is a code block"
    }

.. _cross_reference:

Cross-Reference
---------

.. _role:

Role
----

Roles:

* doc
* ref
* py:func

Pointing to a document in the same dir: :doc:`documentation <documentation>`.

.. _directive:

Directive
---------

Directives:

* py:function
* autofunction
* autoexception

:py:func:`mod.f` is the documentation for the python function ``mod.f()``:

.. py:function:: mod.f(arg=[0])

   Returns 0 if ``arg == ['0']``

   :param arg: An argument of no use.
   :type arg: list[int]
   :raise mod.InvalidArgError: if arg is not [0].
   :return: 0
   :rtype: list[int]

notice that the function raises an exception :py:exc:`mod.InvalidArgError`:

.. py:exception:: mod.InvalidArgError

   Raised if some condition is met.

Notice this can be replaced by fetching the documentation from the function itself:

.. autofunction:: mod.f

.. autoexception:: mod.InvalidArgError

QA
--

Couldn't really understand `doctest <https://www.sphinx-doc.org/en/master/tutorial/describing-code.html#including-doctests-in-your-documentation>`_. Is the purpose to test the code snippets included in the docs? That is amazing, but I couldn't really get it to work. Also, I'm wondering if those code snippets could be imported in docstrings of methods. In a way, these are already unit tests, but not all unit tests are interesting to post in the API reference of the module.