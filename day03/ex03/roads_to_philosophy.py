import requests, sys
from bs4 import BeautifulSoup

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def request_wikipedia(page: str):
	steps = 0
	visited = set()
	start = page
	while page is not None:
		if page in visited:
			print("It leads to an infinite loop !")
			return
		visited.add(page)
		steps += 1

		path = "/wiki/" + page
		URL = f'https://en.wikipedia.org{path}'

		try:
			res = requests.get(url=URL, headers=HEADERS)
			res.raise_for_status()
		except requests.HTTPError as e:
			if (res.status_code == 404):
				return print("It's a dead end !")
		except requests.exceptions.ConnectionError as e:
			return print(e)
		except requests.exceptions.Timeout as e:
			return print(e)
		except requests.exceptions.RequestException:
			return print(e)
		soup = BeautifulSoup(res.text, 'html.parser')
		content = soup.find(id='mw-content-text')
		redirect = soup.find('ul', class_='redirectText')
		if redirect:
			link = redirect.find('a')
			if link and link.get('title'):
				page = link['title']
				continue 
		allLinks = content.select('p > a')
		for link in allLinks:
			if link.find_parent('i') or link.find_parent('em'):
				continue
			if(link.get('title') == 'Philosophy'):
				print(f'{steps} roads from {start} to philosophy')
				return
			if(link.get('href') is not None and link['href'].startswith('/wiki/'))\
					and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
				print(link.get('title'))
				page = link.get('title')
				break
			else:
				print("No result found")
				return

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