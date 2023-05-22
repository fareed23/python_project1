import phonenumbers
from phonenumbers import timezone  # For Time
from phonenumbers import geocoder  # For Location
from phonenumbers import carrier  # For Network

number = "+923333334202"
phone_number = phonenumbers.parse(number)
print(geocoder.description_for_number(phone_number, "en"))
print(timezone.time_zones_for_number(phone_number))
print(carrier.name_for_number(phone_number, "en"))
