from django.shortcuts import render
#from django.http import HttpResponse
from .models import Network, Location, Extra, Station
import requests

API_URL= "http://api.citybik.es/v2/networks/bikesantiago"

def api_bike(request):
    api_data = get_api_data()
    if not api_data:
        return render(request, "apiBike/apibike_error.html")
    data = api_data['network'] 
    
    network = Network()
    network.id_network = data['id']
    network.name = data['name']
    network.company = data['company']
    network.gbfs_href = data['gbfs_href']
    network.href = data['href']
    network.save()

    location = Location()
    location.city = data['location']['city']
    location.country = data['location']['country']
    location.latitude = data['location']['latitude']
    location.longitude = data['location']['longitude']
    location.network = network
    location.save()

    data_stations = data['stations']
    for station in data_stations:
        new_station = Station()
        new_station.id_station = station['id']
        new_station.name = station['name']
        new_station.empty_slots = station['empty_slots']
        new_station.free_bikes = station['free_bikes']
        new_station.latitude = station['latitude']
        new_station.longitude = station['longitude']
        new_station.timestamp = station['timestamp']
        new_station.network = network
        new_station.save()

        extras = station['extra']
        new_extra = Extra()
        new_extra.address = extras['address']
        new_extra.altitude = extras['altitude']
        new_extra.ebikes = extras['ebikes']
        new_extra.has_ebikes = extras['has_ebikes']
        new_extra.last_updated = extras['last_updated']
        new_extra.normal_bikes = extras['normal_bikes']
        new_extra.payment = extras['payment']
        new_extra.payment_terminal = extras['payment-terminal']
        try:
            new_extra.post_code = extras['post_code']
        except:
            new_extra.post_code = "N/A"
        new_extra.renting = extras['renting']
        new_extra.returning = extras['returning']
        new_extra.slots = extras['slots']
        new_extra.uid = extras['uid']
        new_extra.station = new_station
        new_extra.save()
    
    return render(request, "apiBike/apibike.html")


def get_api_data():
    try:
        resp = requests.get(API_URL)
        if resp.status_code == 200:
            api_data = resp.json()
        else:
            raise requests.exceptions.HTTPError
    except requests.RequestException as err:
        # Mejorable, se debe capturar el error especifico
        # y logging de error. mientras, error en consola.
        print("Excepción API Request: \n", err)
        api_data = {}
    finally:
        return api_data
