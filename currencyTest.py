import Currency

ca = Currency.CurrencyAtlas()
IE = ca.getCurrency('United Kingdom')

print(IE.currencyCode)
print(IE.currencyName)
print(IE.currencyRate)
print(IE.currencyRate + 1)
