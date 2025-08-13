import json


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    with open("./data/data.json", "r", encoding="utf-8") as f:
        rates = json.load(f)
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency == to_currency:
        return amount

    if from_currency == "UZS":
        return amount * rates[to_currency]["from_uzs"]

    if to_currency == "UZS":
        return amount * rates[from_currency]["to_uzs"]
    
    amount_in_uzs = amount * rates[from_currency]["to_uzs"]
    return amount_in_uzs * rates[to_currency]["from_uzs"]