from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text

class Page:

	def __init__(self, elem: Elem):
		if not isinstance(elem, Elem):
			raise Elem.ValidationError()
		self.elem = elem

	def __str__(self):
		if isinstance(self.elem, Html):
			return '<!DOCTYPE html>\n' + str(self.elem)
		else:
			return str(self.elem)

	def is_valid(self):
		return self.__is_valid_node(self.elem)

	def write_to_file(self, filename):
		with open(filename, 'w') as f:
			f.write(str(self))

	def __is_valid_node(self, node):
		valid_type = (Html, Head, Body, Title, Meta, Img,
				Table, Th, Tr, Td,
				Ul, Ol, Li,
				H1, H2, P, Div, Span, Hr, Br,
				Text)
		if not isinstance(node, valid_type):
			return False
		
		if isinstance(node, Html):
			if len(node.content) != 2:
				return False
			if not isinstance(node.content[0], Head):
				return False
			if not isinstance(node.content[1], Body):
				return False

		if isinstance(node, Head):
			if len(node.content) != 1:
				return False
			if not isinstance(node.content[0], Title):
				return False
		
		if isinstance(node, (Body, Div)):
			for child in node.content:
				if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
					return False

		if isinstance(node, (Title, H1, H2, Li, Th, Td)):
			if len(node.content) != 1:
				return False
			if not isinstance(node.content[0], Text):
				return False

		if isinstance(node, P):
			for child in node.content:
				if not isinstance(child, Text):
					return False

		if isinstance(node, Span):
			for child in node.content:
				if not isinstance(child, (Text, P)):
					return False

		if isinstance(node, (Ul, Ol)):
			if len(node.content) < 1:
				return False
			for child in node.content:
				if not isinstance(child, Li):
					return False

		if isinstance(node, Tr):
			if len(node.content) < 1:
				return False
			for child in node.content:
				if not isinstance(child, (Th, Td)):
					return False
			first_type = type(node.content[0])
			for child in node.content:
				if type(child) != first_type:
					return False

		if isinstance(node, Table):
			if len(node.content) < 1:
				return False
			for child in node.content:
				if not isinstance(child, Tr):
					return False

		if not isinstance(node, Text) and node.content:
			for child in node.content:
				if not self.__is_valid_node(child):
					return False

		return True
	
if __name__ == '__main__':

	#########	DOCTYPE TEST   #########
	page = Page(Html([
		Head([Title([Text("Hello")])]),
		Body()
	]))
	output = str(page)
	assert output.startswith('<!DOCTYPE html>'), "FAIL — missing doctype"
	print("Test 1 OK - doctype present")

	page = Page(H1([Text("title")]))
	output = str(page)
	assert not output.startswith('<!DOCTYPE html>'), "FAIL — doctype should not be here"
	print("Test 2 OK - no doctype")

	#########	IS VALID TEST   #########
	page = Page(Html([
		Head([Title([Text("Hello")])]),
		Body([Ul([Li([Text("item")])])]),
	]))
	assert page.is_valid() == True, "Fail - Should be valid"
	print("Test 3 OK - valid with ol/ul")

	page = Page(H1([Text("title")]))
	page.elem.content = ["raw string"]
	assert page.is_valid() == False, "FAIL - raw string should be invalid"
	print("Test 4 OK - invalid type detected")

	page = Page(Html([Body(), Head([Title([Text("Hello")])])]))
	assert page.is_valid() == False, "Fail - wrong order should be invalid"
	print("Test 5 OK - wrong order detected")

	page = Page(Html([Head([Title([Text("Hello")])]),Body([Ul([])])]))
	assert page.is_valid() == False, "Fail - empty ul should be invalid"
	print("Test 6 OK - empty ul detected")

	page = Page(Html([Head([Title([Text("Hello")]), Title([Text("World")])]) , Body()]))
	assert page.is_valid() == False, "Fail - two title should be invalid"
	print("Test 7 OK - two title in head detected")

	page = Page(Html([Head([Title([Text("Hello")])]), Body([Table([Tr([Th([Text("h")]), Td([Text("d")])])])])]))
	assert page.is_valid() == False, "Fail - mixed Th and Td should be invalid"
	print("Test 8 OK - mixed Th and Td detected")

	try:
		page = Page("not an elem")
		assert False, "Fail - should have raised ValidationError"
	except Elem.ValidationError:
		print("Test 9 OK - ValidationError raised with string")

	try:
		page = Page(42)
		assert False, "Fail - should have raised ValidationError"
	except Elem.ValidationError:
		print("Test 10 OK - ValidationError raised with int")

	try:
		page = Page(None)
		assert False, "Fail - should have raised ValidationError"
	except Elem.ValidationError:
		print("Test 11 OK - ValidationError raised with None")