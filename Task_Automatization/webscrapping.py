import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.scrapethissite.com/pages/simple/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the country names and save them in a list
country_names = []
for row in soup.select('tr'):
    country_name = row.select_one('td:nth-child(1)').text.strip()
    country_names.append(country_name)

# Save country names to a txt file
with open('country_names.txt', 'w', encoding='utf-8') as file:
    for country_name in country_names:
        file.write(country_name + '\n')

print("Country names saved to 'country_names.txt'.")
