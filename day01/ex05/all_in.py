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

	myList = arg.split(",")
	for i in myList:
		result = i.strip().lower()
		if result == "":
			continue
		found = False

		for key, value in states.items():
			if result == key.lower():
				cap = capital_cities.get(value)
				print(f"{cap} is the capital city of {key}")
				found = True
				break

		if not found:
			for code, city in capital_cities.items():
				if result == city.lower():
					result = []
					for k, v in states.items():
						if v == code:
							result.append(k)
					state = result[0]
					print(f"{city} is the capital city of {state}")
					found = True
					break
		
		if not found:
			print(f"{i.strip()} is neither a capital city nor a state")

if __name__ == '__main__':
	args = sys.argv

	if len(args) != 2:
		sys.exit()
	
	main(sys.argv[1])