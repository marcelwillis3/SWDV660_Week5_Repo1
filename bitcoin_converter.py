# Bitcoin Converter
# Author: Marcel Willis

# Notify the user of the current bitcoin rate (source: Coinbase.com)
print("As of 2/14/2021 at 7:10pm, bitcoin is currently trading at $48,767.60 per bitcoin")

# Allow user to input their number of bitcoins and convert to float
bitcoin = float(input("Enter your bitcoin amount: "))

# Convert bitcoin to US Dollars
bitcoin2USD = round(48767.60*bitcoin,2)

# Return to the user what their bitcoin amounts to in US Dollars
print("That is worth","$",str(bitcoin2USD))