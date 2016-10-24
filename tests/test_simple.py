"""Simple tests just to test the framework."""
# core python libraries
import logging
import os
import unittest
# third party libraries
# custom libraries


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
if 'VERBOSE' in os.environ:
    logger.setLevel(logging.DEBUG)


class TestSimple(unittest.TestCase):
    """Simple test case..."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def simple_test_case(self):
        """Simplest test case."""
        self.assertTrue(True)
