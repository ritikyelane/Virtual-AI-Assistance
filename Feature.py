from project import speak
import webbrowser as web
import requests
import geocoder
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

def GoogleMaps(place):
    url_Place = "https://www.google.com/maps/place/" + str(place)

    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(place , addressdetails=True)

    target_latlon = location.latitude , location.longitude

    location = location.raw['address']

    target = {'city' : location.get('city' , ''),
                'state' : location.get('state',''),
                    'country' : location.get('country' , '')}
    
    current_loca = geocoder.ip('me')
    current_lotlon = current_loca.latlng

    distance = str(great_circle(current_lotlon,target_latlon))
    distance = str(distance.split(' ' , 1)[0])
    distance = round(float(distance),2)

    speak(target)
    speak(f"Sir {place} is {distance} Kilometer away from your location")
GoogleMaps()