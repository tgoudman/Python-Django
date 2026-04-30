def main():
	try:
		with open("numbers.txt") as fd:
			for line in fd.readlines():
				print_line(line)
	except FileNotFoundError:
		print("File not found.")

def print_line(lines: str):
	nodes = lines.split(',')
	for i in nodes:
		print(i)

if __name__ == '__main__':
	main()