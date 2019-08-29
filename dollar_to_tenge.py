from bs4 import BeautifulSoup
import requests
import re

source = "https://fx-rate.net/USD/KZT/"
info = requests.get(source).text
elements = BeautifulSoup(info, 'lxml').find('h1', {"style": "margin-top:5px;color:#ec1b1b;"})
money = re.findall(r"[-+]?\d*\.\d+|\d+", elements.getText())

userinput = float(input('Enter the amount of dollars for translating into tenge:\n'))
print("USD -> KZT:")
print(float(money[1]) * userinput)