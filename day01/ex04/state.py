import sys

def main(arg):
	states = {
		"Oregon"  : "OR",
		"Alabama"  : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for key, value in capital_cities.items():
		if value == arg:
			for state_name, code in states.items():
				if code == key:
					print(state_name)
					return
	print("Unknown capital city")

if __name__ == '__main__':
	args = sys.argv

	if len(args) != 2:
		sys.exit()
	
	main(sys.argv[1])