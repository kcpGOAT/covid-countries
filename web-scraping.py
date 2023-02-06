from bs4 import BeautifulSoup
import requests

covid_table = []
covid_data = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(covid_data.text, "html.parser")

table_soup = soup.find("table", attrs = {"id": "main_table_countries_today"})
rows = table_soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    cols = [x.text.strip() for x in cols]
    covid_table.append(cols)
