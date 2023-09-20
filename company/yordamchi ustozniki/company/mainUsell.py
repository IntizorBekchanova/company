from company import Company
from number import Number

usellFile = open("Usell.txt","r")
usellNumbers = usellFile.readlines()

usell  = Company(companyName="Usell")
price = 1000
for i in usellNumbers:
    price+=100
    usell.addNumber(number=Number(company="Usell",number=i,price=price))


usellPhoneNumbers = usell.getPhoneNumbers()
print(usellPhoneNumbers[0])
usell.sellNumber(usellPhoneNumbers[0])
print(usell)
 