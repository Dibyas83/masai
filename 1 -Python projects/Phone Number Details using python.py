


"""
pip install phonenumbers

"""
import phonenumbers #
from phonenumbers import timezone,geocoder,carrier  # for area time, service provider,sim related info
number = input("Enter your ph no, with +__: ")
phone = phonenumbers.parse(number) # will give details of ph no
time_zone = timezone.time_zones_for_number(phone)
Isp = carrier.name_for_number(phone,"en") # geo or airtel
reg = geocoder.description_for_number(phone,"en") # registrations

print(phone)
print(time_zone)
print(Isp)
print(reg)




















