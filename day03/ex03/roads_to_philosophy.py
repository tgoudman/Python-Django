import requests, sys
from bs4 import BeautifulSoup


def request_wikipedia(page: str):
	steps = 0
	visited = set()
	while page is not None:
		if (steps > 50):
			print('Too many steps, no path found.')
			return
		if page in visited:
			print(f"Loop detected {page}")
			return
		visited.add(page)
		HEADERS = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
		}

		path = "/wiki/" + page
		URL = f'https://en.wikipedia.org{path}'

		try:
			res = requests.get(url=URL, headers=HEADERS)
			res.raise_for_status()
		except requests.HTTPError as e:
			if (res.status_code == 404):
				return print("It's a dead end !")
			return print(e)
		soup = BeautifulSoup(res.text, 'html.parser')
		content = soup.find(id='mw-content-text')
		allLinks = content.select('p > a')
		for link in allLinks:
			if(link.get('title') == 'Philosophy'):
				print('Your are the Goat {steps}')
			if(link.get('href') is not None and link['href'].startswith('/wiki/'))\
					and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
				print(f'[{steps}] {link}')
				page = link.get('title')
				break

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("One argument required")
		sys.exit(1)
	arg = sys.argv[1]
	try:
		request_wikipedia(arg)
	except Exception as e:
		print(e)
		sys.exit(1)