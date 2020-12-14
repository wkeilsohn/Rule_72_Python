# Declare Functions: 
class Rules():
	"Rule of 72"
	std_val = 72

	def get_value(self):
		val = input("Please enter a value: ")
		try:
			val = float(val)
			return val
		except:
			print("You must enter a number. \n")
			self.get_value()

	def calcYear(self):
		interest_rate = self.get_value()
		years = str(self.std_val / interest_rate)
		years = "Estimated number of years to double investment is: " + years
		print(years)

	def calcInterest(self):
		years = self.get_value()
		interest_rate = str(self.std_val / years)
		interest_rate = "Estimated interest rate needed is: " + interest_rate
		print(interest_rate)

class Logic(Rules):
 	"""Logic for Program"""
 	def __init__(self):
 		self.options = ['YES', 'Y'] # More possitive responces can be added later.


 	def processResponce(self, st_ans):
 		st_ans = st_ans.upper()
 		if st_ans in self.options:
 			return True
 		else:
 			return False

 	def sortOptions(self):
 		qa1 = input("Enter 1 to calculate number of years and 2 to calculate amount of interest. [1/2]: ")
 		try:
 			val = int(qa1)
 			if val == 1:
 				self.selectYears()
 			elif val == 2:
 				self.selectInterest()
 			else:
 				print("The option you have selected is not valid. \n")
 				self.sortOptions()
 		except:
 			print("The option you have selected is not valid. \n")
 			self.sortOptions()

 	def selectYears(self):
 		qa2 = input("Would you like to calculate the number of years needed to double your investment based on interest rate? [Y/N]: ")
 		qa2_ans = self.processResponce(qa2)
 		if qa2_ans:
 			print("Please enter rate as a whole number (ex. 10% = 10).")
 			super().calcYear()
 			pass
 		else:
 			self.sortOptions()

 	def selectInterest(self):
 		qa3 = input("Would you like to calculate the interest rate necessary to double your investment in the given time frame? [Y/N]: ")
 		qa3_ans = self.processResponce(qa3)
 		if qa3_ans:
 			print("Please enter number of Years.")
 			super().calcInterest()
 			pass
 		else:
 			self.sortOptions()

 	def continueCheck(self):
 		qa4 = input("Would you like to continue? [Y/N]: ")
 		qa4_ans = qa4.upper()
 		if qa4_ans in self.options:
 			return True
 		else:
 			return False


# Create Instances and enviormental variables
l = Logic()
run_checker = True

# Run Script:

if __name__ == '__main__':
	print("Welcome to the Rule of 72 Calculator!")
	while run_checker:
		l.sortOptions()
		run_checker = l.continueCheck()
		pass