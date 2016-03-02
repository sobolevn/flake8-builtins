# -*- coding: utf-8 -*-

class BuiltinsChecker(object):
    name = 'flake8_builtins'
    version = '0.1'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        pass
