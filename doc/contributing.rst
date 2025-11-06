=========================
Contributing to fairgraph
=========================


Contributions
=============

Contributions are welcome, and credit will always be given.

Report bugs
-----------

Report bugs through `GitHub <https://github.com/HumanBrainProject/fairgraph/issues>`__.

Please report relevant information and preferably code that demonstrates the problem.

Fix bugs or add new features
----------------------------

Look through the GitHub issues for bugs. Anything is open to whoever wants to implement it.
Changes should be proposed through pull requests.

Improve documentation
---------------------

fairgraph could always use better documentation, whether as part of the official docs,
in docstrings, or elsewhere (articles, tutorials, videos).

Submit feedback
---------------

The best way to send feedback is to `open an issue on GitHub <https://github.com/HumanBrainProject/fairgraph/issues/new>`__.

Code of conduct
---------------

We wish to foster an open and welcoming environment within the project.
As such we request that contributors abide by our code of conduct (see :file:`CODE_OF_CONDUCT.md` `(Link) <https://github.com/HumanBrainProject/fairgraph/blob/master/CODE_OF_CONDUCT.md>`_).


Developers' Guide
=================

Setting up a development environment
------------------------------------

We recommend developing in a Python virtual environment.

For example::

    $ python3 -m venv /path/to/venv
    $ source /path/to/venv/bin/activate


Getting the source code
-----------------------

We use the Git version control system. The best way to contribute is through
GitHub. You will first need a GitHub account, and you should then fork the
fairgraph `GitHub Repository`_
(see http://help.github.com/en/articles/fork-a-repo).

To get a local copy of the repository::

    $ cd /some/directory
    $ git clone git@github.com:<username>/fairgraph.git

Now you need to make sure that the ``fairgraph`` package is on your PYTHONPATH.
You can do this by installing with the *editable* option,
which avoids reinstalling when there are changes in the code::

    $ cd fairgraph
    $ pip install -e .

To install all dependencies needed for development::

    $ pip install -e .[dev]

or if using the zsh shell::

    $ pip install -e ".[dev]"

We strongly recommend always working in a branch other than "master", and keeping your
local master branch synchronized with the main, "upstream" repository::

    $ git remote add upstream git@github.com:HumanBrainProject/fairgraph.git
    $ git pull upstream master

    $ git checkout -b informative-branch-name

If the branch is for fixing a bug, we suggest including the word "bug" in the branch name,
or name it after a Github issue, e.g. "issue-42".
If the branch is for adding a new feature, make the branch name a short but informative
description of the feature, e.g. "improve-tests".

Building the openMINDS module
-----------------------------

The :mod:`fairgraph.openminds` module is built from the openMINDS schemas.
To obtain the latest schemas, clone the main openMINDS repository to somewhere
outside the fairgraph directory tree::

    $ git clone https://github.com/openMetadataInitiative/openMINDS.git /path/to/openMINDS

Within the main fairgraph folder::

    $ cd builder
    $ python update_openminds.py /path/to/openMINDS/schemas/v4.0

This will over-write the contents of the :file:`fairgraph/openminds` directory.

Running the test suite
----------------------

Before you make any changes, run the test suite to make sure all the tests pass
on your system. In the top-level fairgrapgh directory, run::

    $ pytest

At the end, if you see "OK", then all the tests
passed (or were skipped because certain dependencies are not installed),
otherwise it will report on tests that failed or produced errors.

To run tests from an individual file::

    $ pytest test/test_properties.py

Coding standards and style
--------------------------

All code should conform as much as possible to `PEP 8`_.
We use black_ to auto-format the code, with a line length of 119 characters.
Please run ``black`` before making a commit.

As a basic check of code quality, run::

    $ flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

Writing tests
-------------

You should try to write automated tests for any new code that you add. If you
have found a bug and want to fix it, first write a test that isolates the bug
(and that therefore fails with the existing codebase). Then apply your fix and
check that the test now passes.

To see how well the tests cover the code base, run::

    $ pytest --cov=fairgraph

Working on the documentation
----------------------------

All modules, classes, functions, and methods (including private and subclassed
builtin methods) should have docstrings.
Please see `PEP 257`_ for a description of docstring conventions.

The documentation is written in `reStructuredText`_, using the `Sphinx`_
documentation system.

To build the documentation::

    $ cd doc
    $ make html

Then open `_build/html/index.html` in your browser.

Committing your changes
-----------------------

Once you are happy with your changes, **run the test suite again to check
that you have not introduced any new bugs**. It is also recommended to check
your code with a code checking program, such as pyflakes or flake8.  Then
you can commit them to your local repository::

    $ git commit -m 'informative commit message'

If this is your first commit to the project, please add your name, ORCID if you have one, and
affiliation/employer to :file:`doc/authors.json`

You can then push your changes to your online repository on GitHub::

    $ git push origin informative-branch-name

(A reminder that we recommend working in a git branch other than "master").
Once you think your changes are ready to be included in the main fairgraph repository,
open a pull request on GitHub
(see https://help.github.com/en/articles/about-pull-requests).


Dealing with pull requests
--------------------------

Anyone is welcome to review a pull request, although only project maintainers are able to merge them.

- do the CI test pass?
- review the code - at least one person
- give feedback - be sure to thank the contributor, especially if it is a first time contribution!

Making a release
----------------

Add a section in :file:`/doc/release_notes.rst` for the release.

First check that the version string (in :file:`pyproject.toml` and :file:`fairgraph/__init__.py`) is correct.

To build source and wheel packages::

    $ python -m build

Tag the release in the Git repository and push it::

    $ git tag <version>
    $ git push --tags origin
    $ git push --tags upstream

To upload the package to `PyPI`_ (the members of the `maintainers team`_ have the necessary permissions to do this)::

    $ twine upload dist/fairgraph-x.y.z.tar.gz dist/fairgraph.x.y.z-py3-none-any.whl

Governance
----------

fairgraph is maintained by Andrew Davison.
If the project begins to attract a larger number of regular contributors
we will transition to a more democratic governance model.
The copyright is held jointly by all contributors and/or their employers at the time of contribution,
as listed in :file:`doc/authors.rst`.
fairgraph is licenced under the Apache Software Licencse v2.0.


.. _`GitHub Repository`: https://github.com/HumanBrainProject/fairgraph/
.. _`PEP 8`: https://pypi.org/project/pep8/
.. _`maintainers team`: https://github.com/orgs/HumanBrainProject/teams/fairgraph-maintainers
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://www.sphinx-doc.org/
.. _`PEP 257`: https://www.python.org/dev/peps/pep-0257/
.. _black: link/to/black
.. _PyPI: https://pypi.org
