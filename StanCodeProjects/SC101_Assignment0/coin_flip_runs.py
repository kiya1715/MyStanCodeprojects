"""
File: coin_flip_runs.py
Name: Karen
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program will show the result of selecting "H" or "T" randomly with the number of runs input by users.
	A 'run' is defined as consecutive results on either 'H' or 'T'
	And this program will show the result when it reach the number of runs.
	"""
	# Ask user input the number of runs
	print("Let's flip a coin!")
	data = int(input('Number of runs: '))
	num_run = 0
	switch = False
	roll1 = random_chr()
	line = roll1

	while num_run != data:
		roll2 = random_chr()

		if roll1 == roll2:
			if not switch:
				num_run += 1
				switch = True
			line += roll2

		else:
			line += roll2
			switch = False
			roll1 = roll2

	print(str(line))

def random_chr():
	# Decided the "H" or "T" randomly and return the result
	chr = r.randrange(1,3)
	if chr == 1:
		return "T"
	return "H"


# def random_chr():





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
