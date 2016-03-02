# -*- coding: utf-8 -*-
from flake8_builtins import BuiltinsChecker
from tempfile import mkdtemp

import os
import unittest


class TestBuiltins(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
