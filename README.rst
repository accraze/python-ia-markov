========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-ia-markov/badge/?style=flat
    :target: https://readthedocs.org/projects/python-ia-markov
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-ia-markov.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/python-ia-markov

.. |requires| image:: https://requires.io/github/accraze/python-ia-markov/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/accraze/python-ia-markov/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/accraze/python-ia-markov/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/accraze/python-ia-markov

.. |codecov| image:: https://codecov.io/github/accraze/python-ia-markov/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/accraze/python-ia-markov

.. |version| image:: https://img.shields.io/pypi/v/ia-markov.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ia-markov

.. |downloads| image:: https://img.shields.io/pypi/dm/ia-markov.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/ia-markov

.. |wheel| image:: https://img.shields.io/pypi/wheel/ia-markov.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/ia-markov

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ia-markov.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ia-markov

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ia-markov.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ia-markov


.. end-badges

A Markov model trained on Internet Archive text files.

* Free software: BSD license

Installation
============

::

    pip install ia-markov

Quick Start
===========

::

    import ia_markov

    m = MarkovModel()
    m.train_model('FuturistManifesto')
    m.model.make_sentence()
    'Courage, audacity, and revolt will be drunk with love and admiration for us.'


Documentation
=============

https://python-ia-markov.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
