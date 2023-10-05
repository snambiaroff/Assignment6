sum = 0
product = 1

while True:
  number = input("Enter a number (press q to quit): ")

  if number == "q":
    break

  number = int(number)

  sum += number
