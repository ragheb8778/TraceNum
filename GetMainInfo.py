number = input("Enter the TARGET with <+>: " )
import phonenumbers
import number
print(number)
print("......................")

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber,"en"))
print("......................")

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
print("......................")
print("")

import sys
sys.exit()
