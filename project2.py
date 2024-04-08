#Bike Rental System
class bikeShop:
	def _init_(self,stock):
		self.stock=stock
		def displayBike(self):
			print("Total Bikes",self.stock)
			def rentForBike(self,q):
				if q<=0:
					print("Enter the postive value or gratern than zero.")
				elif q>self.stock:
					print("Enter the value (less then stock)")
				else:
					print("Total Pirces",q*500)
					print("Total Bikes",self.stock)

while True:
     obj=bikeShop(100)
     uc=int(input('''
1.Display BikeStocks
2.Rent a Bike
3. Exit
		'''))
     if uc==1:
	     obj.displayBike()
     elif uc==2:
	     n=int(input("Enter the Qty:-"))
	     obj.rentForBike(n)
	     

