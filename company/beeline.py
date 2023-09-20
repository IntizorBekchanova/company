from amaliyot1 import Company
from Number import Number

beelineFile = open("Beeline.txt", "r")
beelineNumbers = beelineFile.readlines()

beeline = Company(company_name="beeline.py")
price = 1000
for i in beelineNumbers:
    price += 100
    beeline.addNumbers(number = Number(Company = "Beeline", number = i, price = price))
    


















