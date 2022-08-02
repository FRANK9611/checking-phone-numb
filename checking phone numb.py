import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo = phonenumbers.parse(input("Enter the phone number with country code"))
print (timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo,"en"))
print(geocoder.description_for_number(mobileNo,"en"))
print("valid mobile no: ", phonenumbers.is_valid_number(mobileNo))


print("checking possiblity of number: ", phonenumbers.is_valid_number(mobileNo))
