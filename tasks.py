"""
`invoke <https://www.pyinvoke.org/>`_ is the project's task runner. The tasks are defined at ``tasks.py``.
"""
from invoke import task
import os

@task
def docs(ctx, step='build'):
    """Documentation ops.

    :param ctx: _description_
    :type ctx: _type_
    :param step: ``build`` to build the docs, ``clean`` to remove the built 
    docs, defaults to ``build``.
    :type step: str, optional
    """
    if step == 'build':
        cmds = [
            "cd docs/sphinx",
            "make html",
            "cp -a _build/html/. ..",
            "make clean",
            "echo && echo && echo && echo Your static documentation pages can be found at \'docs\' \(Ctrl+Click\) && echo",
        ]
    elif step == 'clean':
        cmds = [
            "cd docs/sphinx",
            "make clean",
            "cd ..",
            "rm -rf src .buildinfo _sources _static .nojekyll genindex.html index.html objects.inv search.html searchindex.js py-modindex.html",
        ]

    ctx.run(';'.join(cmds))
