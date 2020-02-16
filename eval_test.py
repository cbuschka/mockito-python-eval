from mockito import when, mock, verify
import unittest


class SUT:
  def __init__(self, collab):
    self.collab = collab

  def ask(self):
    return self.collab.ask()


class EvalTest(unittest.TestCase):
  def setUp(self):
    self.collab = mock()
    self.sut = SUT(collab=self.collab)

  def test_mock_called(self):
    self.sut.ask()
    verify(self.collab, times=1).ask()

  def test_mock_behaviour(self):
    when(self.collab).ask().thenReturn("yes")
    answer = self.sut.ask()
    self.assertEqual(answer, "yes")


if __name__ == '__main__':
    unittest.main()
