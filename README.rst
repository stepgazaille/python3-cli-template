Python3 CLI template
********************
Project tagline goes here.

.. image:: https://travis-ci.org/stepgazaille/python3-cli-template.svg?branch=master
    :target: https://travis-ci.org/stepgazaille/python3-cli-template

.. contents:: **Contents of this document**
   :depth: 2


Description
===========
Project description goes here.


Installation
============

Use the following commands to install the program (assumes virtual env):

.. code:: shell

    git clone https://github.com/stepgazaille/python3-cli-template.git
    cd python3-cli-template
    pip install .


Documentation
=============
API documentation
-----------------
The `API documentation <https://stepgazaille.github.io/python3-cli-template/>`_ is hosted on `GitHub Pages <https://pages.github.com/>`_


Usage
-----

.. code:: shell

   usage: program-cli [-h] [-o OPTIONAL] mandatory

   program -- program description

   Created by John Doe on 2016-09-03.
   Copyright 2016. All rights reserved.

   Licensed under the Apache License 2.0
   http://www.apache.org/licenses/LICENSE-2.0

   Distributed on an "AS IS" basis without warranties
   or conditions of any kind, either express or implied.

   USAGE

   positional arguments:
     mandatory             A mandatory argument.

   optional arguments:
     -h, --help            show this help message and exit
     -o OPTIONAL, --optional OPTIONAL
                           an optional argument


Usage examples
~~~~~~~~~~~~~~

Use case no 1:

.. code:: shell

    program-cli "mandatory argument"

Use case no 2:

.. code:: shell

    program-cli "mandatory argument" -o "optional argument"


Contributing to the project
===========================
Installation
------------

Use the following command to install testing and documentation dependencies (assumes virtual env):

.. code:: shell

    pip install -r requirements.txt


Use the following commands to install the program in editable mode (assumes virtual env):

.. code:: shell

    git clone https://github.com/stepgazaille/python3-cli-template.git
    cd python3-cli-template
    pip install -e .


Testing
-------
Style checker
~~~~~~~~~~~~~

We are using `pep8 <https://pypi.python.org/pypi/pep8>`_ for style checking. Use the following command to check style:

.. code:: shell

    pep8 .


Bad code smells
~~~~~~~~~~~~~~~

We are using `pylint <https://www.pylint.org/>`_ to catch bad code smells. Use the following command to catch bad code smells:

.. code:: shell

    pylint ./program/


Unit testing
~~~~~~~~~~~~

We are using `nose2 <https://github.com/nose-devs/nose2>`_ for unit testing. Use the following command to run unit tests:

.. code:: shell

    nose2


End-to-end testing
~~~~~~~~~~~~~~~~~~
Use the following command to run end-to-end tests:

.. code:: shell

    python3 ./tests/end_to_end_test.py


Generating documentation
------------------------
We are using `Sphinx <http://www.sphinx-doc.org>`_ to generate our API documentation. Use the following commands to generate a local version of the project's API documentation:

.. code:: shell

    cd docs
    make clean; make html

The generated API documentation will appear in docs/_build/html/ directory.


Versioning
==========
We are using  `SemVer <http://semver.org>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/stepgazaille/python3-template/tags>`_


Author
======

- **Stephane Gazaille** - *Initial work*


License
=======
This project is licensed under the Apache License Version 2.0. See `LICENSE <https://github.com/stepgazaille/python3-template/blob/master/LICENSE>`_ for details
