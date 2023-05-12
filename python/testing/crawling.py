import requests
from bs4 import BeautifulSoup

response = requests.get("censored(originally url)")
soup = BeautifulSoup(response.content, "html.parser")

transaction = soup.select(
    "h2#pagevolumewhereamountexist(censored) + h3 + table > tbody tr td:nth-child(7) span"
)

# list comprehension & generation expression
total_amount = sum(int(amount.text.replace(",", "")) for amount in transaction)

print(f"예시 페이지 내 거래총량은 {total_amount:,} 회입니다.")

# https://colab.research.google.com/drive/1sqWp-CZa7i1u7RqAekxg97b-QUh-Ltr-#scrollTo=58YglaVo_S-x
