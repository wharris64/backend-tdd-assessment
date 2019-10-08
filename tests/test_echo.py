#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class testing_testing(unittest.TestCase):

    def setUp(self):
        # self.parser = echo.create_parser()
        pass

    def test_help(self):
        """ Running the program without arguments should show usage. """

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        args = ["-u", "hello"]
        # namespace = self.parser.parse_args(args)

        # self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

    def test_lower(self):
        args = ["-l", "HELLO"]
        self.assertEquals(echo.main(args), "hello")
        # self.assertFalse(echo.main('Hello'))

    # def test_title(self):
    #     self.assertEqual(hello,Hello)
    # def test_allargs(self):
    #     args = ["-u", "-t", "-l", "heLLo"]
    #     self.assertEquals(echo.main(args), "hello")
    def test_title(self):
        args = ["-t", 'hello world']
        self.assertEquals(echo.main(args), "Hello World")

    def test_all(self):
        args = ["-ult", "hello duder"]
        self.assertEquals(echo.main(args), "Hello Duder")

    def test_none(self):
        args = ['hello']
        self.assertEquals(echo.main(args), 'hello')


if __name__ == '__main__':
    unittest.main()
