from intefaces import BaseSupplier
from typing import Any, Dict, List
from models import Hotel,Location,Amenities

class Acme(BaseSupplier):
    @staticmethod
    def endpoint() -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
    
    def parse(self, obj: Dict[str,Any]) -> Hotel:
        data = { 
            "id": obj["Id"],
            "destination_id": obj["DestinationId"],
            "name": obj["Name"],
            "location": {
                "lat": obj.get("Latitude",None),
                "lng": obj.get("Longitude",None),
                "address": obj["Address"],
                "city": obj["City"],
                "country": obj["Country"],
            },
            "description": obj['Description'],           
            "amenities": {
                "general" : obj['Facilities'],
                "room" : []
            },
            "images" : {
                'rooms': [],
                'amenities': [],
                'site': []
                
            },
            "booking_conditions" :[],
            "supplier_name" : self.__class__.__name__
        }

        return Hotel(**data)
    
    # Example implementation of fetch method
class Paperflies(BaseSupplier):
    @staticmethod
    def endpoint() -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"
    
    def parse(self, obj: Dict[str,Any]) -> Hotel:
        rooms_img = []
        site_img = []
        amenities_img = []
        for i in obj['images']['rooms'] :
            rooms_img.append({'link' : i['link'], 'description' : i['caption']})
        for i in obj['images']['site'] :
            site_img.append({'link' : i['link'], 'description' : i['caption']})
        data = {
            'id': obj['hotel_id'],
            'destination_id': obj['destination_id'],
            'name': obj['hotel_name'],
            'location': {
                "address" : obj['location']['address'],
                "country": obj['location']['country'],
            },
            'description' : obj['details'],
            'amenities': {
                "general": obj['amenities']['general'],
                "room": obj['amenities']['room'],
            },
            'images' : {
                'rooms': rooms_img ,
                'amenities': amenities_img,
                'site': site_img,
            },
            'booking_conditions' : obj['booking_conditions'],
            "supplier_name" : self.__class__.__name__
        }
        return Hotel(**data)

class Patagonia(BaseSupplier) :
    @staticmethod
    def endpoint() -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"
    
    def parse(self, obj: Dict[str,Any]) -> Hotel:
        
        rooms_img = []
        site_img = []
        amenities_img = []
        for i in obj['images']['rooms'] :
            rooms_img.append({'link' : i['url'], 'description' : i['description']})
        for i in obj['images']['amenities'] :
            amenities_img.append({'link' : i['url'], 'description' : i['description']})
        data = {
            'id' : obj['id'],
            'destination_id' : obj['destination'],
            'name' : obj['name'],
            'location' : {
                'lat' : obj['lat'],
                'lng' : obj['lng'],
                'address' : obj.get('address',''),
            }, 
            'description' : obj.get('info',''),
            'amenities' : {
                "general" : obj.get('amenities',[]),
            },
            'images' : {
                'rooms': rooms_img ,
                'amenities': amenities_img,
                'site': site_img,
            },
            "supplier_name" : self.__class__.__name__
        }
        if data['description'] is None :
            data['description'] = ''
        return Hotel(**data)