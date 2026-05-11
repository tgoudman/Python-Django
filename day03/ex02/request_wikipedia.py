import requests, json, sys, dewiki

def request_wikipedia(page: str):
	URL = "https://en.wikipedia.org/w/api.php"

	HEADERS = {
		"User-Agent": "MyScript/1.0"
	}
	PARAMS = {
		"action": "parse",
		"page": page,
		"prop": "wikitext",
		"format": "json",
		"redirects": "true"
	}

	try:
		res = requests.get(url=URL, params=PARAMS, headers=HEADERS)
		res.raise_for_status()
	except requests.HTTPError as e:
		raise e
	try:
		data = res.json()
	except json.JSONDecodeError as e:
		raise e
	if data.get("error") is not None:
		raise Exception(data["error"]["info"])
	wikitext = data['parse']['wikitext']['*']
	text_clean = dewiki.from_string(wikitext)
	return text_clean

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("One argument required")
		sys.exit(1)
	arg = sys.argv[1]
	try:
		wiki_data = request_wikipedia(arg)
	except Exception as e:
		print(e)
		sys.exit(1)
	try:
		arg = arg.replace(' ', '_')
		f = open("{}.wiki".format(arg), "w")
		f.write(wiki_data)
		f.close()
	except Exception as e:
		print(e)
	