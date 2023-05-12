import requests
from bs4 import BeautifulSoup
from datetime import datetime

start_date = datetime(2019, 9, 24)
end_date = datetime(2019, 10, 23)

url = "https://paullab.co.kr/stock.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    date_str = cols[0].text.strip()
    date = datetime.strptime(date_str, "%Y.%m.%d")

    if start_date <= date <= end_date:
        volume = cols[1].text.strip()
        print(f"Date: {date_str}, 거래량: {volume}")
