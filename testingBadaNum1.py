import unittest
import random
from BadaNumNeelabh1 import *
class NamesTestCase(unittest.TestCase):
	def test_first_last_name1(self):
		n = input("No of time you want to test the case: ")
		for i in range(int(n)):
			a= random.randint(-100000000000000000000000000000,10000000000000000000000000000000000000)
			b=random.randint(-10000000000000000000000000000000,100000000000000000000000000000000000000)
			n1=bigNum()
			n2=bigNum()
			n1.setInput(a)
			n2.setInput(b)
			n3=addBigNum(n1,n2)
			n4=subBigNum(n1,n2)
			print("a:"+str(a)+"\nb:"+str(b)+"\na+b: "+str(a+b)+"\nGiven output: "+n3.returnStringOutput()+"\n"+n4.returnStringOutput()+"\n")
			self.assertEqual(int(n3.returnStringOutput()),(a+b))
			self.assertEqual(int(n4.returnStringOutput()),(a-b))



unittest.main()