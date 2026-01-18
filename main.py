import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://nationalbank.kz/rss/rates_all.xml"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")

        usd = soup.find("title", string="USD")
        rate = usd.find_next("description").text

        return float(rate)

    def convert_to_usd(self, amount):
        return amount / self.usd_rate


def main():
    converter = CurrencyConverter()

    print(f"Текущий курс USD: {converter.usd_rate} KZT")

    amount = float(input("Введите сумму в тенге: "))
    result = converter.convert_to_usd(amount)

    print(f"{amount} KZT = {result:.2f} USD")


if __name__ == "__main__":
    main()
