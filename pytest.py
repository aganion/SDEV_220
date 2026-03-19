"""Alicia Ganion
M_5 Programming Assignment
March 18, 2026

Testing program.py using unit testing and integration testing
"""

import unittest
from program import accuse_suspect

#this is unit testing
class TestDetectiveLogic(unittest.TestCase):
    def test_accuse_evidence_motive(self):
        self.assertTrue(accuse_suspect(3, True, False))
    def test_accuse_evidence_motive2(self):
        self.assertTrue(accuse_suspect(2, True, False))
    def test_scene_of_crime(self):
        self.assertTrue(accuse_suspect(1, False, False))
    def test_scene_of_crime2(self):
        self.assertTrue(accuse_suspect(3, False, True))

if __name__ == '__main__':
    unittest.main()

#This is integration testing

from program import accuse_suspect
def test_cases():
    assert accuse_suspect(1, False, False) == False
    assert accuse_suspect(2, False, False) == False
    assert accuse_suspect(3, True, False) == True
    assert accuse_suspect(2, True, True) == True
    assert accuse_suspect(3, False, False) == False