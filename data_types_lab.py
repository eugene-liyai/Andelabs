def data_type(val):
	
	if val is None:
		return 'no value'

	elif isinstance(val, list):
		return val[2] if len(val) > 2 else None

	elif isinstance(val, bool):
		return val

	elif isinstance(val, int):
		if val < 100:
			return 'less than 100'
		elif val > 100:
			return 'more than 100'
		else:
			return 'equal to 100'
	elif isinstance(val, str):
		return len(val)

if __name__ == '__main__':
	print(data_type(100))