# Install the forex-python library before running the script
# pip install forex-python

from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")
    
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
