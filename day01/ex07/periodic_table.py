def ft_print(dictionnary : dict):
	for key, attributs in dictionnary.items():
		print(key)
		for key, value in attributs.items():
			print(key, value)
		print('\n')

def generate_html(tableau):

	fd = open("periodic_table.html", "w")
	fd.write("<!DOCTYPE html>\n")
	fd.write('<html lang="en">\n')
	fd.write("\t<head>\n")
	fd.write('\t\t<meta charset="UTF-8">\n')
	fd.write('\t\t<title>Periodic Table</title>\n')
	fd.write('\t\t<link rel="stylesheet" href="periodic_table.css">\n')
	fd.write("\t</head>\n")
	fd.write("<body>\n")
	fd.write("\t<table>\n")

	for ligne in tableau:
		fd.write("\t\t<tr>\n")

		for cell in ligne:
			if cell is None:
				fd.write('\t\t\t<td class="empty"></td>\n')
			else:
				name ,attributs = cell
				number = attributs["number"]
				fd.write(f'\t\t\t<td id="number{number}">\n')
				fd.write(f"\t\t\t\t<h4>{name}</h4>\n")
				fd.write("\t\t\t\t\t<ul>\n")
				for key, value in attributs.items():
					if key == "number":
						fd.write(f"\t\t\t\t\t\t<li>No {value}</li>\n")
					elif key == "small":
						fd.write(f'\t\t\t\t\t\t<li class="small">{value}</li>\n')
					elif key == "molar":
						fd.write(f"\t\t\t\t\t\t<li>{value}</li>\n")
					elif key == "electron":
						fd.write(f"\t\t\t\t\t\t<li>{value} electron</li>\n")
					elif key == "position":
						pass
				fd.write("\t\t\t\t\t</ul>\n")
				fd.write("\t\t\t</td>\n")

		fd.write("\t\t</tr>\n")
	fd.write("\t</table>\n")
	fd.write("</body>\n")
	fd.write("</html>\n")
	fd.close()

	
def build_table(dictionnaire):
	tableau = []
	ligne = []
	position_previous = -1

	for nom, attributs in dictionnaire.items():
		position_actual = int(attributs["position"])

		if position_actual <= position_previous:
			tableau.append(ligne)
			ligne = []
			position_previous = -1

		empty_case = position_actual - position_previous - 1
		for i in range(empty_case):
			ligne.append(None)

		ligne.append((nom, attributs))
		position_previous = position_actual
	
	tableau.append(ligne)
	return tableau


def parse():
	try:

		fd = open("periodic_table.txt", "r")
		dict = {}
		for line in fd.readlines():
			result = line.split("=")
			nom = result[0].strip()
			atributs = {}

			for paire in result[1].split(","):
				resultPaire = paire.split(":")
				atributs[resultPaire[0].strip()] = resultPaire[1].strip()
			dict[nom] = atributs
	except FileNotFoundError:
		print("File not found.")
		exit()
	
	return dict

def main():
	d = parse()
	tableau = build_table(d)
	generate_html(tableau)

if __name__ == '__main__':
	main()