import random
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate

class CoffeeMachine:
	def __init__(self):
		self.brokenCount = 10
	def repair(self):
		self.brokenCount = 10
	def serve(self, drink: HotBeverage):
		if (self.brokenCount <= 0):
			raise CoffeeMachine.BrokenMachineException()
		self.brokenCount -= 1
		if random.randint(0, 1) == 0:
			return CoffeeMachine.EmptyCup()
		return drink()

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90
		def description(self):
			return ("An empty cup?! Gimme my money back!")
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

if __name__ == '__main__':
	coffeeMachineTest = CoffeeMachine()
	for i in range(30):
		try:
			print(f"\033[32mTEST no {i}\033[0m")
			print(coffeeMachineTest.serve(random.choice([Coffee, Tea, Cappuccino, Chocolate])))
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			coffeeMachineTest.repair()