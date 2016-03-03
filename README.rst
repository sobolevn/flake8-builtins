.. -*- coding: utf-8 -*-

.. image:: https://travis-ci.org/gforcada/flake8-builtins.svg?branch=master
   :target: https://travis-ci.org/gforcada/flake8-builtins

.. image:: https://coveralls.io/repos/gforcada/flake8-builtins/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/gforcada/flake8-builtins?branch=master

Flake8 Builtins plugin
======================
Check for python builtins being used as variables or parameters.

Given the following code::

    def my_method(object, list, dict):
        max = 5
        min = 3
        zip = (4, 3)

The following warnings are shown (via flake8)::

   test.py:1:15: B002 "object" is used as an argument and thus shadows a python builtin, consider renaming the argument
   test.py:1:23: B002 "list" is used as an argument and thus shadows a python builtin, consider renaming the argument
   test.py:1:29: B002 "dict" is used as an argument and thus shadows a python builtin, consider renaming the argument
   test.py:2:5: B001 "max" is a python builtin and is being shadowed, consider renaming the variable
   test.py:3:5: B001 "min" is a python builtin and is being shadowed, consider renaming the variable
   test.py:4:5: B001 "zip" is a python builtin and is being shadowed, consider renaming the variable

Install
-------
Install with pip::

    $ pip install flake8-builtins

Requirements
------------
- Python 2.7, 3.3, 3.4
- flake8

License
-------
GPL 2.0
