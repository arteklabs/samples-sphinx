"""
Task Runner
===========

About
-----

The |project| uses `invoke <https://www.pyinvoke.org/>`_ as the task runner. List the available tasks:

.. code:: shell

   $ inv --list
   Available tasks:

   docs        Documentation

Requirements
------------

* :doc:`installation`

Getting Started
---------------

The tasks are defined at :download:`tasks.py <../../../../tasks.py>` and are listed below:

.. autofunction:: docs(step='build', port=docker_host_sphinx_server_default_port, verbose=False)
"""
import logging
import os
import sys
import tabulate
import json

from invoke import task

logging.basicConfig(
    format="%(asctime)s %(levelname)s: (%(filename)s:%(lineno)d) %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("root")

docs_docker_image = "python:3.8"
docs_debug_container_name = "arteklabs_sphinx_docs"
sphinx_server_default_port = "8000"
docker_host_sphinx_server_default_port = "8040"
docs_debug_mnt_path = f"{os.getcwd()}/docs/sphinx/_build/html"
docs_debug_container_path = "/root"

# utils
pad = lambda msg: f"\n\n\t{msg}\n"


def find_version(*file_paths):
    version_match = r"^__version__ = ['\"]([^'\"]*)['\"]"
    parent = os.path.abspath(os.path.dirname(__file__))
    version_file = read(*file_paths, here=parent)
    version_match = re.search(version_match, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read(*parts, here):
    return codecs.open(os.path.join(here, *parts), "r").read()


@task
def test(ctx, verbose=False, test=None,):
    """Run unit tests.

    Parameters
    ----------
    verbose : bool, optional
        _description_, by default False
    test : string, optional
        The test name, by default None (run all tests).
    """
    cmds =[]
    if test:
        cmds = [
            "pytest --cov=src -k {}".format(test)
        ]
    else:
        cmds = [
            "pytest --cov=src",
            "coverage html --directory docs/sphinx/_static/html/coverage",
            "coverage erase",
        ]

    if verbose:
        res = ctx.run(" && ".join(cmds))
    else:
        res = ctx.run(" && ".join(cmds), hide="both")

@task
def quality(ctx, verbose=False):
    """Run unit tests.

    Parameters
    ----------
    verbose : bool, optional
        _description_, by default False
    """
    cmds = [
        "radon cc src",
        "radon mi src",
        "radon raw src",

        "radon cc tests",
        "radon mi tests",
        "radon raw tests",

        "radon cc docs",
        "radon mi docs",
        "radon raw docs",

        "radon cc tasks.py",
        "radon mi tasks.py",
        "radon raw tasks.py",

        "vulture src",
        "vulture tests",
        "vulture docs",
        "vulture tasks.py",

        "bandit src",
        "bandit tests",
        "bandit docs",
        "bandit tasks.py",
    ]

    if verbose:
        ctx.run(" && ".join(cmds))
    else:
        ctx.run(" && ".join(cmds), hide="both")


@task
def lint(ctx, verbose=False, commit=False):
    """Lint the |project|'s source code.

    Parameters
    ----------
    verbose : bool, optional
        _description_, by default False
    commit : bool, optional
        If ``True``, the linting changes are commited, by default ``False``
    """
    cmds = [
        "black src",
        "black docs",
        "black tests",
        "black tasks.py",

        "isort src",
        "isort docs",
        "isort tests",
        "isort tasks.py",
    ]
    if verbose:
        res = ctx.run(" && ".join(cmds))
    else:
        res = ctx.run(" && ".join(cmds), hide="both")

    if commit:
        cmds = [
            "git add docs tests tasks.py src",
            "git commit -m 'auto: lint'",
        ]
        if verbose:
            res = ctx.run(" && ".join(cmds))
        else:
            res = ctx.run(" && ".join(cmds), hide="both")


@task
def docs(ctx, step="build", port=docker_host_sphinx_server_default_port, verbose=False):
    """Documentation Operations

    Documentation
    =============

    The task ``docs`` encapsulates all the logic related to developing, building, testing and publishing the project docs.

    Build
    -----

    Builds the docs and checks for WARNINGS or ERRORS.

    .. code:: shell

        inv docs --step build [--verbose]

    Example

    .. code:: shell

       $ inv docs --step build
       2023-02-20 18:25:16,293 INFO: (tasks.py:256)

           build ✔️

    Copy
    ----

    Copies the built docs into ``docs``. This step is temporary until the docs
    are adequately built into an S3 location, and are not persisted in the repo.

    .. code:: shell

        inv docs --step copy [--verbose]

    Example

    .. code:: shell

       $ inv docs --step copy
       2023-02-20 18:25:16,293 INFO: (tasks.py:256)

           copy ✔️

    Preview
    -------

    Builds the docker image and runs the container to preview the docs with a contaneirized sphinx server listening on 0.0.0.0:``port``. Preview the docs with:

    .. code:: shell

        inv docs --step preview --port {locally-available-port}

    Example

    .. code:: shell

       $ inv docs --step build
       inv docs --step preview
       local sphinx run: OK
       container: dmacli_docs
       host: http://0.0.0.0:8000
       stop: inv docs --stop

    Clean
    -----

    Remove all the static pages.

    Stop Preview
    ------------

    Stop the local preview container with a sphinx python server.

    .. code:: shell

        inv docs --step stop-preview

    Example

    .. code:: shell

       $ inv docs --step stop-preview
       dmaclidocs

    :param step: The docs tasks step: ``build``, ``publish``, ``preview``, ``stop-preview``, ``deploy``, ``destroy``. Defaults to ``build``.
    :type step: str, optional
    :param verbose: Log verbose information. Defaults to ``False``.
    :type verbose: bool, optional
    """
    if step == "build":

        test(ctx, verbose)

        cmds = [
            "cd docs/sphinx",
            "make html",
        ]

        if verbose:
            res = ctx.run(" && ".join(cmds))
        else:
            res = ctx.run(" && ".join(cmds), hide="both")

        if "WARNING" in res.stdout:
            sys.exit(
                "There seems to be a WARNING in the build process. Please fix it before publishing the docs. Add the flag '--verbose' to see the stdout."
            )
        elif res.stderr:
            sys.exit("There seems to be an ERROR in the build process. Add the flag '--verbose' to see the stderr.")

        logger.info(pad("build ✔️"))

    if step == "copy":

        cmds = ["cp -R docs/sphinx/_build/html/* docs/"]

        if verbose:
            res = ctx.run(" && ".join(cmds))
        else:
            res = ctx.run(" && ".join(cmds), hide="both")

        logger.info(pad("copy ✔️"))

    if step == "preview":
        cmd = f"""
        # run container it it doesn't exist locally already
        if [[ "docker container inspect -f '{{{{.State.Running}}}}' {docs_debug_container_name}" != "true" ]]; then
            docker run \
                --rm \
                -d \
                --name {docs_debug_container_name} \
                -p 0.0.0.0:{port}:{sphinx_server_default_port} \
                --mount type=bind,source={docs_debug_mnt_path},target={docs_debug_container_path} \
                {docs_docker_image} \
                sleep infinity
        fi

        # have the container running the sphinx server
        docker exec \
            -d \
            -w {docs_debug_container_path} \
            {docs_debug_container_name} \
            python -m http.server
        """
        if verbose:
            ctx.run(cmd)
        else:
            ctx.run(cmd, hide="both")

        logger.info(
            f"""
            local sphinx run ✔️
            container: {docs_debug_container_name}
            host: http://0.0.0.0:{docker_host_sphinx_server_default_port}
            stop: inv docs --stop
        """
        )

    if step == "stop-preview":
        ctx.run(f"docker stop {docs_debug_container_name}")

    if step == "clean":
        cmds = [
            "cd docs/sphinx",
            "make clean",
            "cd ..",
            "rm -rf _downloads",
            "rm -rf _images",
            "rm -rf src",
            "rm -rf .buildinfo",
            "rm -rf _sources",
            "rm -rf _static",
            "rm -rf genindex.html",
            "rm -rf index.html",
            "rm -rf objects.inv",
            "rm -rf search.html",
            "rm -rf searchindex.js",
            "rm -rf py-modindex.html",
        ]

        if verbose:
            res = ctx.run(" && ".join(cmds))
        else:
            res = ctx.run(" && ".join(cmds), hide="both")

        logger.info(pad("local clean ✔️"))
