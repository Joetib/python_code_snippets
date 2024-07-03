# We can use the `forex-python` library to convert currency exchange rates.
# Install the library using:
# >> pip install forex-python

from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Convert the amount from one currency to another
amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted_amount = c.convert(from_currency, to_currency, amount)

# Print the converted amount
print(converted_amount)

# Output
# >> 85.0
# Please Like and Subscribe