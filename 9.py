#13-Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="http")
loc1=input("enter your first city")
loc2=input("enter your second city")
location1 = geolocator.geocode(loc1)
location2=geolocator.geocode(loc2)
a=(location1.latitude,location1.longitude)
b=(location2.latitude,location2.longitude)
print(a)
print(b)
print(geodesic(a,b).miles)
