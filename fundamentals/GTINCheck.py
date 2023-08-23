def is_valid_gtin(gtin):
  """Checks if a GTIN code is valid.

  Args:
    gtin: The GTIN code to check.

  Returns:
    True if the GTIN code is valid, False otherwise.
  """

  if len(gtin) != 13:
    return False

  checksum = 0
  for i in range(1, 13):
    if i % 2 == 0:
      digit = int(gtin[i]) * 3
    else:
      digit = int(gtin[i])

    if digit > 9:
      digit = digit - 9

    checksum += digit

  return checksum % 10 == 0


if __name__ == "__main__":
  print(is_valid_gtin("07506246000055"))
