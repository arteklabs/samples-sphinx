Arteklabs Samples: Sphinx
=========================

Read the docs `here <https://arteklabs.github.io/samples-sphinx/>`_.

:rst syntax:

      TODO

:github-pages publish:

      TODO

:bootstrap python docs on your python projects:

   TODO

:vscode python docstring format:

   see settings.json for mustache file

:vscode extensions:

   python

:importing rst files outside of docs:

   TODO

:variables in conf.py:

  see conf.py and rst_epilog

:module docs pointer to module function:

  see tasks.py module docstring ``.. autofunction``
  see conf.py ``sys.path.insert(0, os.path.abspath('../..'))``

.. warning::

   notice the tasks.py docstring pointing to itself as a download. This will fail if the file's docstrings are imported from different rst locations. Unless:

   .. code-block:: text

      Here's the extracted docs:

      .. automodule:: tasks
         :noindex:
         :members:

:links:
  
  see docs/sphinx/links

:autodoc:

  vscode python extension
  sphinx autodoc extension
  settings.json
  notice that the docs on the docstring look like crap but theyre rendered beautifully

:css:

  TODO

:import rst file outside of docs:

  see docs/sphinx/index.rst

:import docstrings:

   docs/sphinx/src/api.rst imports src/main.py

   notice that src/main.py doesnt import directly src/utils/arithmetic.py. Because we want to subdivide the reference
   in separate pages, we need to add .rst pages that import src/utils/arithmetic.py. src/main.py will point to these
   rst pages instead.

   notice that the module doc imports the module components docs one by one (autofunction), not the rst file directly.

   .. code-block:: text

      src
      ├── main.py # module docstring
      ├── sphinx
      └── utils
         └── arithmetic.py # module and members docstring

      docs/sphinx/src
      ├── api
      │   └── utils.rst # imports src/utils/arithmetic.py module (not members)
      ├── api.rst # imports src/main.py module (not members)
      ├── development.rst
      ├── references.rst
      ├── rest.rst
      └── userguide.rst

:point to source code:

   extensions: sphinx.ext.autodoc, sphinx.ext.linkcode
   add resolver to conf.py (specifcy the release branch!)

System Dependencies
===================

* docker (requires pre-installation)
* other dependencies specified in ``pyproject.toml``
