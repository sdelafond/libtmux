.. module:: libtmux

.. _developing:

======================
Developing and Testing
======================

.. todo::
    link to sliderepl or ipython notebook slides

Our tests are inside ``tests/``. Tests are implemented using
`pytest`_.

``make test`` will create a tmux server on a separate ``socket_name``
using ``$ tmux -L test_case``.

.. _pytest: http://pytest.org/

.. _install_dev_env:

Install the latest code from git
--------------------------------

To begin developing, check out the code from github:

.. code-block:: bash

    $ git clone git@github.com:tony/libtmux.git
    $ cd libtmux

Now create a virtualenv, if you don't know how to, you can create a
virtualenv with:

.. code-block:: bash

    $ virtualenv .venv

Then activate it to your current tty / terminal session with:

.. code-block:: bash

    $ source .venv/bin/activate

Good! Now let's run this:

.. code-block:: bash

    $ pip install -e .

This has ``pip``, a python package manager install the python package
in the current directory. ``-e`` means ``--editable``, which means you can
adjust the code and the installed software will reflect the changes.

.. code-block:: bash

    $ libtmux

Test Runner
-----------

As you seen above, the ``libtmux`` command will now be available to you,
since you are in the virtual environment, your `PATH` environment was
updated to include a special version of ``python`` inside your ``.venv``
folder with its own packages.

.. code-block:: bash

    $ make test

You probably didn't see anything but tests scroll by.

If you found a problem or are trying to write a test, you can file an
`issue on github`_.

.. _test_specific_tests:

Test runner options
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ py.test tests/test_common.py

will test the ``tests/test_common.py`` tests.

.. code-block:: bash

    $ py.test tests/test_common.py::test_ignores_letter_versions

tests ``test_ignore_letter_versions()`` ``tests/test_common.py``.

Multiple can be separated by spaces:

.. code-block:: bash

    $ py.test tests/test_{window,pane}.py \
      tests/test_common.py::test_ignores_letter_versions

.. _test_builder_visually:

Visual testing
~~~~~~~~~~~~~~

You can watch tmux testsuite build sessions visually by keeping a client
open in a separate terminal.

Create two terminals:

  - Terminal 1: ``$ tmux -L test_case``
  - Terminal 2: ``$ cd`` into the libtmux project and into the
    ``virtualenv`` if you are using one, see details on installing the dev
    version of libtmux above. Then:

    .. code-block:: bash
    
        $ py.test tests/test_workspacebuilder.py

Terminal 1 should have flickered and built the session before your eyes.
libtmux hides this building from normal users.

Run tests on save
-----------------

You can re-run tests automatically on file edit.

.. note::
    This requires ``entr(1)``.

Install `entr`_.  Packages are available available on most Linux and BSD
variants, including Debian, Ubuntu, FreeBSD, OS X.

To run all tests upon editing any ``.py`` file:

.. code-block:: bash

    $ make watch_test

.. _entr: http://entrproject.org/

Rebuild the documentation when an ``.rst`` file is edited:

.. code-block:: bash

   $ cd doc
   $ make watch

.. _libtmux developer config:

libtmux developer config
------------------------

After you :ref:`install_dev_env`, when inside the libtmux checkout:

.. code-block:: bash

    $ libtmux load .

this will load the ``.tmuxp.yaml`` in the root of the project.

.. literalinclude:: ../.tmuxp.yaml
    :language: yaml

.. _travis:

Travis CI
~~~~~~~~~

libtmux uses `travis-ci`_ for continuous integration / automatic unit
testing.

libtmux is tested against tmux 1.8 and the latest git source. Interpretters
tested are 2.6, 2.7 and 3.3. The `travis build site`_ uses this
`.travis.yml`_ configuration:

.. literalinclude:: ../.travis.yml
    :language: yaml

.. _travis-ci: http://www.travis-ci.org
.. _travis build site: http://www.travis-ci.org/tony/libtmux
.. _.travis.yml: https://github.com/tony/libtmux/blob/master/.travis.yml
.. _issue on github: https://github.com/tony/libtmux/issues
