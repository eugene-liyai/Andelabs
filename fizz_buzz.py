def fizz_buzz(val):

	# check fizzbuzz for specific inputs 
	if val%5 == 0 and val%3 == 0:
		return 'FizzBuzz'
	# check if divisible by three
	elif val%3 == 0:
		return 'Fizz'
	# check if divisible by five
	elif val%5 == 0:
		return 'Buzz'
	else:
		return val