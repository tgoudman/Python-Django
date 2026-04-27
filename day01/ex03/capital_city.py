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

	for key, value in states.items():
		if key == arg:
			print(capital_cities.get(value))
			return
	print("Unknown state")

if __name__ == '__main__':
	args = sys.argv

	if len(args) != 2:
		sys.exit()
	
	main(sys.argv[1])