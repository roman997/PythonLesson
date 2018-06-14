class Machine:
	def __init__(self, machineName, price, status):
		self.machineName = machineName
		self.price = price
		if status == "ready":
			self.ready = True
		else:
			self.ready = False