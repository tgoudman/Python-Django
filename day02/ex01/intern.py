class Intern:
	def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
		self.name = name
	def __str__(self):
		return self.name
	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	def make_coffee(self):
		return self.Coffee()

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

if __name__ == '__main__':
	myIntern = Intern()
	try:
		myIntern.work()
	except Exception as e:
		print(e)
	print(myIntern)
	coffee = myIntern.make_coffee()
	print(coffee)