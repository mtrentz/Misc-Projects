import re
import csv
import pandas as pd

"""
My take on this regex challenge:

Validate the IBAN code: GB82 WEST 1234 5698 7654 32
"""

# CSV with country codes
codes = pd.read_csv('countrycodes.csv')

list_of_countries = codes.Code.tolist()

def reg_gen(country_list):
    """ Generates a regex viable country codes. """
    country_pattern = "("
    for c in country_list:
        country_pattern += str(c) + "|"
    country_pattern = country_pattern[:-1]
    country_pattern+= ")"
    return country_pattern

country_regex = reg_gen(list_of_countries)
pattern = country_regex+"[0-9]{2}\s*[a-zA-Z]{4}\s*[0-9]{4}\s*[0-9]{4}\s*[0-9]{4}\s*[0-9]{2}"

IBAN = "GB82 WEST 1234 5698 7654 32"

if re.match(pattern, IBAN):
    print("Match!")
else:
    print('IBAN does not match')
