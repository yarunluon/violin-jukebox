class MockDigitalInOut:
  """Mock class for testing"""

  # Members
  value = None

class Human:
  """Simulate human behavior"""

  # Constants
  TOUCH = 1
  NO_TOUCH = 0

  def touch(self, pad):
    pad.value = self.TOUCH

  def stop_touching(self, pad):
    pad.value = self.NO_TOUCH