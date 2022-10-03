.. raw:: html

   <a href="https://github.com/lifespline/samples-sphinx.git"><img loading="lazy" width="149" height="149" src="https://github.blog/wp-content/uploads/2008/12/forkme_left_darkblue_121621.png?resize=149%2C149" class="attachment-full size-full" alt="Fork Me On Github" data-recalc-dims="1"></a>


==========
RST Syntax
==========

Below, you'll find a set of samples of the ``reST`` syntax with snippets.


Core Concepts
-------------

You'll find literature on these concepts at :doc:`literature`

.. _include_rst_file:

Including a Rest File Outside The Root Dir
------------------------------------------

Given ``docs/sphinx/conf.py`` and ``docs/sphinx/index.rst``, add ``app/README.rst`` by creating ``docs/sphinx/link.rst`` such that:

.. code-block:: rst

    .. include:: ../../app/README.rst

Edit ``docs/sphinx/index.rst`` such that:

.. code-block:: rst

    .. toctree::
        :maxdepth: 1
        :caption: Contents:

        link

Edit ``docs/sphinx/conf.py`` such that:

.. code:: python 

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../..'))


.. _inline_ext_link:

Root
----

This is the root document.

.. _paragraph:

Paragraph
---------

The basic block in a reST document.

.. _inline_markup:

Inline Markup
-------------

*italics*, **bold** and ``code``

.. code::

    *italics*, **bold** and ``code``

.. _list:

List
----

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

.. code::

    * This is a bulleted list.
    * It has two items, the second
      item uses two lines.
    
    1. This is a numbered list.
    2. It has two items too.
    
    #. This is a numbered list.
    #. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

.. code::

    * this is
    * a list
    
      * with a nested list
      * and some subitems
    
    * and here the parent list continues

.. _definitions:

Definition
----------

definition (up to a line of text)
   Multiline definition of the definition (indented)

   multiline definition of the definition

definition
   definition of the definition

.. code::

    definition (up to a line of text)
       Multiline definition of the definition (indented)
    
       multiline definition of the definition
    
    definition
       definition of the definition

| These lines are
| broken exactly like in
| the source file.

.. code::

    | These lines are
    | broken exactly like in
    | the source file.

.. _literal_paragraph:

Literal Paragraph
-----------------

standard paragraph::

   multiline literal paragraph

   multiline literal paragraph

standard paragraph

.. _doctest_block:

Doctest Block
-------------

Doctest blocks are interactive Python sessions cut-and-pasted into docstrings. They do not require the literal blocks syntax. The doctest block must end with a blank line and should not end with an unused prompt.

>>> 1 + 1
2

.. code:: python

    >>> 1 + 1
    2

.. _table:

Table
-----

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

.. code::

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

.. code::

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

.. _hyperlink:

Hyperlink
---------

web link: `Link text <https://domain.invalid/>`_

.. code::

    `Link text <https://domain.invalid/>`_

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

.. code::

    This is a paragraph that contains `a link`_.

    .. _a link: https://domain.invalid/

.. _domain:

Domain
------

`read the docs <https://www.sphinx-doc.org/en/master/glossary.html#term-domain>`_

.. _section:

Section
-------

.. code::

    Section
    -------

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=`` for sections
* ``-`` for subsections
* ``^`` for subsubsections
* ``"`` for paragraphs

.. _code:

Code block
----------

.. code:: bash

    echo "this is a code block"

.. code-block:: json

    {
        "this": "is a code block"
    }

.. _internallink:

Cross Reference
---------------

Types of cross references:

* :ref:`Internal <cross_references_internal>`
* :ref:`Documents <cross_references_docs>`
* :ref:`Objects: Python <cross_reference_objects_python>`
* :ref:`Objects: JS <cross_reference_objects_js>`

.. _cross_references_internal:

Cross-Reference: Internal
-------------------------

Referencing the :ref:`next paragraph <next_paragraph>`.

.. _next_paragraph:

The next paragraph.

.. code::

    Referencing the :ref:`next paragraph <next_paragraph>`.

    .. _next_paragraph:

    The next paragraph.

.. _cross_references_docs:

Cross-Reference: Documents
--------------------------

Pointer to the ``rst`` document :doc:`literature.rst <literature>`

.. code::

    Pointer to the ``rst`` document :doc:`docs/src/contributing/literature.rst <literature>`

Pointer to the non-``rst`` document :download:`sphinx conf <../conf.py>`

.. code::

    Pointer to the non-``rst`` document :download:`sphinx conf <../conf.py>`

.. _cross_reference_objects_python:

Cross-Reference Objects: Python
-------------------------------

.. code::

    :py:mod:
    :py:func:
    :py:data:
    :py:const:
    :py:class:
    :py:meth:
    :py:attr:
    :py:exc:
    :py:obj:

Examples

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

.. _cross_reference_objects_js:

Cross-Reference Objects: Javascript
-----------------------------------

.. code::

    :js:mod:
    :js:func:
    :js:meth:
    :js:class:
    :js:data:
    :js:attr:

.. _field:

Field
-----

:fieldname: Field content

.. code::

    :fieldname: Field content

tocdepth
    The maximum depth for a table of contents of this file.

.. code::

    :tocdepth: 2

nocomments
    If set, the web application won’t display a comment form for a page generated from this source file.

.. code::

    :nocomments:

orphan
    If set, warnings about this file not being included in any toctree will be suppressed.

.. code::

    :orphan:

nosearch
    If set, full text search for this file is disabled.

.. code::

    :nosearch:

.. _role:

Role
----

Inline piece of explicit markup. See :ref:`Inline Markup <inline_markup>`.

.. _explicit_markup:

Explicit Markup
---------------

An explicit markup block begins with a line starting with ``..``.

.. _directive:

Directive
---------

A directive is a generic block of explicit markup. See :ref:`Explicit Markup <explicit_markup>`.

.. _note:

Note
----

.. note::

    this is a note

.. code::

    .. note::

        this is a note

.. _warning:

Warning
-------

.. warning::

    this is a warning

.. code::

    .. warning::

        this is a warning

.. _image:

Image
-----

Adding an image from an ``url``:

.. image:: https://www.sphinx-doc.org/en/master/_static/sphinxheader.png
    :width: 400
    :alt: Sphinx Logo

.. code::

    .. image:: https://www.sphinx-doc.org/en/master/_static/sphinxheader.png
        :width: 400
        :alt: Sphinx Logo

Adding an image from the ``project repo``:

.. image:: ../static/img/sphinxheader.webp
    :width: 400
    :alt: Sphinx Logo

.. code::

    .. image:: ../static/img/sphinxheader.webp
        :width: 400
        :alt: Sphinx Logo

.. _footnote:

Footnote
--------

text [#fn1]_ text [#fn2]_ text [#]_ text [#]_ text

.. rubric:: Footnotes

.. [#fn1] footnote 1 content
.. [#fn2] footnote 2 content
.. [#] footnote 3 content
.. [#] footnote 4 content

.. code::

    text [#fn1]_ text [#fn2]_ text [#]_ text [#]_ text

    .. rubric:: Footnotes

    .. [#fn1] footnote 1 content
    .. [#fn2] footnote 2 content
    .. [#] footnote 3 content
    .. [#] footnote 4 content

.. _comments:

Comments
--------

..
    multiline comment
    multiline comment

    multiline comment

.. code::

    ..
        multiline comment
        multiline comment

        multiline comment


QA
--

Couldn't really understand `doctest <https://www.sphinx-doc.org/en/master/tutorial/describing-code.html#including-doctests-in-your-documentation>`_. Is the purpose to test the code snippets included in the docs? That is amazing, but I couldn't really get it to work. Also, I'm wondering if those code snippets could be imported in docstrings of methods. In a way, these are already unit tests, but not all unit tests are interesting to post in the API reference of the module.