def palindrome(num: int) -> bool:
  if num < 0:
    return False
  current = num
  reversed_num = 0

  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit

    num = num // 10

  return reversed_num == current


print(palindrome(121))