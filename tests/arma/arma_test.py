# Bulletproof Arma Launcher
# Copyright (C) 2016 Lukasz Taczuk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import unittest
from nose.plugins.attrib import attr

from third_party.arma import Arma


class ArmaTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa_custom_path_none(self):
        """Attention: This test has to be run as the first of custom_path tests!"""
        custom_path = Arma.get_custom_path()
        self.assertIsNone(custom_path)

    def test_custom_path(self):
        path1 = 'asd'
        Arma.set_custom_path(path1)
        got_path1 = Arma.get_custom_path()
        self.assertEqual(got_path1, path1)

        path2 = 'ert'
        Arma.set_custom_path(path2)
        got_path2 = Arma.get_custom_path()
        self.assertEqual(got_path2, path2)

    def test_custom_path_instances(self):
        a = Arma()
        b = Arma()
        Arma.set_custom_path("123")
        c = Arma()

        self.assertEqual(a.get_custom_path(), "123")
        self.assertEqual(b.get_custom_path(), "123")
        self.assertEqual(c.get_custom_path(), "123")
        self.assertEqual(Arma.get_custom_path(), "123")
