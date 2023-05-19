"""Sphinx config file."""
import os
import sys
import codecs
import re
sys.path.insert(0, os.path.abspath('../..')) # task runner docs and utils
sys.path.insert(0, os.path.abspath('../../src'))

def find_version(*file_paths):
    version_match = r"^__version__ = ['\"]([^'\"]*)['\"]"
    parent = os.path.abspath(
        os.path.join(
            os.path.join(os.path.dirname(__file__), os.pardir),
            os.pardir
        )
    )
    version_file = read(*file_paths, here=parent)
    version_match = re.search(version_match, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def read(*parts, here):
    return codecs.open(os.path.join(here, *parts), 'r').read()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Arteklabs Samples: Sphinx'
copyright = '2022, arteklabs'
author = 'arteklabs'
release = find_version("src", "__init__.py")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # display docs build time
    'sphinx.ext.duration',

    # process python docstrings in src
    'sphinx.ext.autodoc',

    # test code snippets
    'sphinx.ext.doctest',

    # adding an explicit target to each section and making sure is unique
    "sphinx.ext.autosectionlabel",

    # link to source code
    # 'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode',
]
autosectionlabel_prefix_document = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# variables
rst_epilog = f"""
.. |project| replace:: ``{project}``
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_logo": "logomark-black@2x.png",
    "dark_logo": "logomark-orange@2x.png",
}
html_title = project
def linkcode_resolve(domain, info):
    """source code url resolver

    .. note::

       the release branch is 'latest', this information could be fetched from the repo
       programatically.

    Parameters
    ----------
    domain : _type_
        _description_
    info : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    pass
    if domain == 'py' and info['module']:
        src=info['module'].replace('.', '/')
        url=f"https://github.com/arteklabs/samples-sphinx/blob/latest/src/{src}.py"
        return url
