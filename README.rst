Python3 project
***************

.. image:: https://travis-ci.org/stepgazaille/python3-template.svg?branch=master
    :target: https://travis-ci.org/stepgazaille/python3-template


My Python3 project template.


.. contents:: **Contents of this document**
   :depth: 2


Installation
============

Use the following commands to install the program:

.. code:: shell

    git clone https://github.com/stepgazaille/python3-template.git
    cd python3-template
    sudo pip3 install .


Usage
=====

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
--------------

Use case no 1:

.. code:: shell

    program-cli mandatory-arg -o optional-arg


Contributing to the project
===========================

Use the following command to install testing and documentation dependencies:

.. code:: shell

    sudo pip3 install -r requirements.txt

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


Documentation
-------------

Generating the project's documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are using `Sphinx <http://www.sphinx-doc.org>`_ to generate our API documentation. Use the following commands to generate a local version of the project's API documentation:

.. code:: shell

    cd docs
    make clean; make html

The generated API documentation will appear in docs/_build/html/ directory.

Hosting
~~~~~~~
The project `online documentation <https://stepgazaille.github.io/python3-template//>`_ is hosted on `GitHub Pages <https://pages.github.com/>`_


Versioning
==========
We use `SemVer <http://semver.org>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/stepgazaille/python3-template/tags>`_

Author
======

- **John Doe** - *Initial work*
