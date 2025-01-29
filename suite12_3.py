import unittest
from unittest.runner import TextTestRunner

from tests_12_2 import RunnerTest, TournamentTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(RunnerTest))

suite.addTest(unittest.makeSuite(TournamentTest))

runner = TextTestRunner(verbosity=2)

runner.run(suite)
