# Create three empty lists
even_numbers = []
odd_numbers = []
prime_numbers = []

# Iterate over the range(1,101)
for number in range(1,101):
  # Check if the number is even
  if number % 2 == 0:
    # Add the number to the even_numbers list
    even_numbers.append(number)
  # Otherwise, the number is odd
