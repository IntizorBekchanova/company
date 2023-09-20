import os 
os.system("cls")
from datetime import date
from number import Number


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.establishedAt = data.today()   # aynan hozirgi vaqt
        self.__phone_numbers = []   #telefon raqamlari aynan listda boladi
        self.__budjet = 0   # byudjet boshida nol boladi

    def setPhoneNumbers(self,numbers): # set metodi ichida ozgartiradi
        self.__phone_numbers = numbers

    def getPhoneNumbers(self):  # get metodi har doim return qaytaradi
        return self.__phone_numbers

    def setBudget(self,money):
        self.__budjet = money 

    def getBudget(self):
        return self.__budget

    def addNumber(self,number:Number):
        self.__phone_numbers.append(number)

    def sellNumber(self,number:Number):
        if number in self.__phone_numbers:
            self.__phone_numbers.remove(number)
            self.budget += number.getPrice()

    def __str__(self) -> str:
        return f"{self.company_name} has been established at {self.establishedAt} and today it has {len(self.__phone_numbers)} numbers and budget ${self.__budjet}"