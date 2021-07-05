from datetime import date as d

import requests
from bs4 import BeautifulSoup

try:
    country = str(input("Enter country: "))
    choice = int(input("Enter relevant number: Total cases (1), New cases (2), Total Deaths (3), New Deaths (4): "))

    today = d.today()

    url = 'https://www.worldometers.info/coronavirus/'
    r = requests.get(url)
    c = r.text
    soup = BeautifulSoup(c, 'html.parser')
    table = soup.find('tbody')
    all_info = table.find_all('tr')
    for each in all_info:
        bar = each.find_all('td')
        name = bar[1].text
        total_cases = bar[2].text
        new_cases = bar[3].text
        total_deaths = bar[4].text
        new_deaths = bar[5].text
        if name == country and choice == 1:
            print(f'Total cases in {country} for {today} is {total_cases}')
        elif name == country and choice == 2:
            print(f'New cases in {country} for {today} is {new_cases}')
        elif name == country and choice == 3:
            print(f'Total deaths in {country} for {today} is {total_deaths}')
        elif name == country and choice == 4:
            print(f'New deaths in {country} for {today} is {new_deaths}')


except ValueError:
    print("Please enter number")
