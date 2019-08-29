from bs4 import BeautifulSoup
import requests
import re

source = "https://fx-rate.net/USD/KZT/"
info = requests.get(source).text
elements = BeautifulSoup(info, 'lxml').find('h1', {"style": "margin-top:5px;color:#ec1b1b;"})
money = re.findall(r"[-+]?\d*\.\d+|\d+", elements.getText())

print("Currently 1 dollar equals to " + money[1] + " tenge")
print("Select option [1] to translate USD -> KZT")
print("Select option [2] to translate KZT -> USD")

select = int(input())

if(select == 1):
	userinput = float(input('Enter the amount of USD for translating into KZT:\n'))
	print(float(money[1]) * userinput)
else:
	userinput = float(input('Enter the amount of KZT to translate into USD:\n'))
	print(userinput / float(money[1]))
