from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
html_data = requests.get(url)

soup = BeautifulSoup(html_data.content, 'html.parser')
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

rows = []
rows = soup.find_all('tbody')[3].find_all(['tr'])
for i in range(1, len(rows)):
    bank_name = rows[i].find_all('td')[1].find_all('a')[1].text
    marker_cap = float(rows[i].find_all('td')[2].text)
    data = data.append({"Name": bank_name, "Market Cap (US$ Billion)": marker_cap}, ignore_index=True)

file = data.to_json('./export.json',orient='index')