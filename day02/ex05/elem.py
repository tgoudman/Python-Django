class Text:
	def __init__(self, text):
		self.text = text
	def __str__(self):
		return f'"{self.text}"'

class Elem:

	class ValidationError(Exception):
		pass

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		self.tag = tag
		self.attr = attr
		self.content = content if content is not None else []
		self.tag_type = tag_type
	def __str__(self):
		if self.attr:
			attrs = " " + "".join(f'{key}="{value}"' for key, value in self.attr.items())
		else:
			attrs = ""
		if self.tag_type == 'simple':
			return f"<{self.tag}{attrs} />"
		else:
			result = f"<{self.tag}{attrs}>\n"
			for child in self.content:
				for line in str(child).split('\n'):
					result += '  ' + line + '\n'
			result += f"</{self.tag}>"
			return result
	def add_content(self, var):
		if isinstance(var, (Elem, Text)):
			self.content.append(var)
		else:
			raise Elem.ValidationError()

class Html(Elem):
	def __init__(self, content=None):
		super().__init__('html', {}, content)

class Head(Elem):
	def __init__(self, content=None):
		super().__init__('head', {}, content)

class Body(Elem):
	def __init__(self, content=None):
		super().__init__('body', {}, content)

class Title(Elem):
	def __init__(self, content=None):
		super().__init__('title', {}, content)

class H1(Elem):
	def __init__(self, content=None):
		super().__init__('h1', {}, content)

class Img(Elem):
	def __init__(self, attr={}):
		super().__init__('img', attr, tag_type='simple')

if __name__ == '__main__':
	page = []
	title = Title([Text("Hello ground!")])
	head = Head([title])
	textH1 = Text("Oh no, not again!")
	h1 = H1([textH1])
	img = Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
	body = Body([h1, img])
	page = Html([head, body])
	print(page)