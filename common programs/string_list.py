"""
Checks whether a luterals are alphanumeric and numbers should be less than or equal to 5.
"""

def str_to_list(str):
	s = []
	for i in str:
		try:
			if int(i) <= 5:
				s.append(i)
		except ValueError as e:
			if i.isalnum():
				s.append(i)
	print(s)
if __name__ == "__main__":
	str_to_list('hello!2#43457893./\[][3')