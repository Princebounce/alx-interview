#!/usr/bin/python3
"""

"""

def validUTF8(data):
  """
  Determines if a given data set represents a valid UTF-8 encoding.

  Args:
    data: A list of integers representing the data.

  Returns:
    True if data is a valid UTF-8 encoding, else return False.
  """

  # Check if the data is empty.
  if not data:
    return False

  # Check if the first byte of the data is a valid UTF-8 start byte.
  if not (data[0] & 0x80 == 0x00):
    return False

  # Check if the remaining bytes of the data are valid UTF-8 continuation bytes.
  for byte in data[1:]:
    if not (byte & 0xc0 == 0x80):
      return False

  return True

