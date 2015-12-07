#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_py-pkgversion
----------------------------------

Tests for `py-pkgversion` module.
"""
import os
import unittest

from pkgversion import (
    get_git_repo_dir, get_version, list_requirements, pep440_version,
    write_setup_py,
)

requirements_file = os.path.join(
    os.path.dirname(__file__), 'fixtures/requirements.txt'
)

setup_py_expected_output = """
from setuptools import setup
setup(**{'install_requires': ['test'], 'version': '1.0.0'})
"""


class TestPkgversion(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_version(self):
        self.assertRegexpMatches(get_version(), r'^(\d.\d(.\d))?(-\d+-\w+)?')

    def test_pep440_version(self):
        assert pep440_version('1.2') == '1.2'
        assert pep440_version('1.2.3') == '1.2.3'
        assert pep440_version('1.2.3-99-ge3b6e92') == '1.2.3+99.ge3b6e92'
        assert pep440_version(None) is None

    def test_list_requirements(self):
        actual = list_requirements(requirements_file)
        expected = [
            'unversioned', 'pinned-version==1.0',
            'ranged-version<=2,>=1.0', 'url', 'unversioned-url',
            'editable'
        ]
        assert actual == expected

    def test_get_git_repo_dir(self):
        assert os.path.isdir(get_git_repo_dir())
        assert os.path.isdir(os.path.join(get_git_repo_dir(), '.git'))

    def test_get_git_repo_dir_invalid(self):
        pwd = os.getcwd()
        os.chdir('/tmp')
        assert get_git_repo_dir() == None
        os.chdir(pwd)

    def test_write_setup_py(self):
        tmp_file = os.tempnam()
        write_setup_py(
            file=tmp_file,
            version='1.0.0',
            install_requires=['test']
        )
        try:
            with open(tmp_file, 'r') as f:
                assert f.read() == setup_py_expected_output
        finally:
            os.remove(tmp_file)


if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
