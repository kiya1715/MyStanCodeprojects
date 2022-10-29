"""
File: largest_digit.py
Name: Karen Chang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	This program recursively confirms and prints the biggest digit in integers.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function will call a helper function to recursively confirms and returns the biggest digit in the param 'n'

	:param n: int, A string of random numbers.
	:return: int, The largest number in the data 'n'
	"""

	# max_number is the biggest digit in the given data which default is 0
	max_number = 0
	new_max_number = find_largest_digit_helper(n, max_number)
	return new_max_number


def find_largest_digit_helper(n, max_number):
	"""
	This is a helper function for confirming the biggest digit recursively.

	:param n: int, A string of random numbers.
	:param max_number: int, The biggest digit in the given data
	:return: int, The final biggest digit in the given data after confirming
	"""
	# If 'n' is a negative number, change it to a positive number
	if n < 0:
		n = -n

	# If 'n' is a positive number
	# Base case
	if n == 0:
		return max_number

	# Not base case
	else:
		# Confirm the place value of ones by dividing by 10
		compare_number = n % 10

		# Compare the value
		if compare_number > max_number:
			max_number = compare_number
		ans = find_largest_digit_helper(int(n/10), max_number)

		# Return the answer
		return ans


if __name__ == '__main__':
	main()
