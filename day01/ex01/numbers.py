def main():
	with open("day01/ex01/numbers.txt") as fd:
		for line in fd.readlines():
			print_line(line)

def print_line(lines: str):
	nodes = lines.split(',')
	for i in nodes:
		print(i)

if __name__ == '__main__':
	main()