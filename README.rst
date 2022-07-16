""""""""""""""""""""""""""""""""""""""""""
Plugin for WDL linting with ``pre-commit``
""""""""""""""""""""""""""""""""""""""""""

This repository provides a plugin for `pre-commit`_ to
perform `miniwdl`_ check on WDL files.


.. _pre-commit: https://pre-commit.com/
.. _miniwdl: https://github.com/chanzuckerberg/miniwdl

=====
Usage
=====

To include this hook, add this ``repo:`` entry to the ``repos`` list in
``.pre-commit-config.yaml`` in the root of your repository:

.. code:: yaml

  repos:
  -   repo: https://github.com/cvaske/miniwdl-pre-commit.git
      rev: v1.6.0
      hooks:
      -   id: miniwdl-check

=================
Versioning policy
=================

Tags here should correspond to the same tag in the miniwdl repository. The
python package is a shell that installs the corresponding miniwdl version for the `pre-commit`.
