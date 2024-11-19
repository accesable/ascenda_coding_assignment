from dataclasses import dataclass
import json
import argparse

import requests
from typing import List, Dict

class Location:
    def __init__(self, lat: float = 0, lng: float = 0, address: str = '', city: str = '', country: str = ''):
        self.lat = lat
        self.lng = lng
        self.address = address
        self.city = city
        self.country = country
    def to_dict(self):
        return {
            'lat': self.lat,
            'lng': self.lng,
            'address': self.address,
            'city': self.city,
            'country': self.country
        }

class Amenities:
    def __init__(self, general: List[str] = [], room: List[str] = []):
        self.general = general
        self.room = room
    def to_dict(self):
        return {
            'general': self.general,
            'room': self.room
        }

class Image:
    def __init__(self, link: str = '', description: str = ''):
        self.link = link
        self.description = description
    def to_dict(self):
        return {
            'link': self.link,
            'description': self.description
        }

class Images:
    def __init__(self, rooms: List[Image] = [], site: List[Image] = [], amenities: List[Image] = []):
        self.rooms = rooms
        self.site = site
        self.amenities = amenities
    def to_dict(self):
        return {
            'rooms': [img.to_dict() for img in self.rooms],
           'site': [img.to_dict() for img in self.site],
            'amenities': [img.to_dict() for img in self.amenities]
        }

class Hotel:
    def __init__(
        self,
        id: str = '',
        destination_id: int = '',
        name: str = '',
        description: str = '',
        location: Dict = None,
        amenities: Dict = None,
        images: Dict = None,
        booking_conditions: List[str] = [],
        supplier_name : str = ''
    ):
        self.id = id
        self.destination_id = destination_id
        self.name = name
        self.description = description
        self.location = Location(**location)
        self.amenities = Amenities(**amenities)
        self.images = Images(
            rooms=[Image(**img) for img in images['rooms']],
            site=[Image(**img) for img in images['site']],
            amenities=[Image(**img) for img in images['amenities']]
        )
        self.booking_conditions = booking_conditions
        self.supplier_name = supplier_name  # Added a new attribute for provider name, which will be used for filtering purposes.
    
    def to_dict(self):
        return {
            'id': self.id,
            'destination_id': self.destination_id,
            'name': self.name,
            'description': self.description,
            'location': self.location.to_dict(),
            'amenities': self.amenities.to_dict(),
            'images': self.images.to_dict(),
            'booking_conditions': self.booking_conditions
        }
    def __str__(self):
            return f"""
Hotel: {self.name}
ID: {self.id}
Destination ID: {self.destination_id}
Description: {self.description[:100]}...
Location: {self.location.lat}, {self.location.lng}, {self.location.address}, {self.location.city}, {self.location.country}
General Amenities: {', '.join(self.amenities.general[:5])}...
Room Amenities: {', '.join(self.amenities.room[:5])}...
Number of Images:
- Rooms: {len(self.images.rooms)}
- Site: {len(self.images.site)}
- Amenities: {len(self.images.amenities)}
Booking Conditions: {len(self.booking_conditions)}
Supplier Name: {self.supplier_name}
            """
# Example of instantiating the Hotel class
data = {
    "id": "iJhz",
    "destination_id": 5432,
    "name": "Beach Villas Singapore",
    "location": {
        "lat": 1.264751,
        "lng": 103.824006,
        "address": "8 Sentosa Gateway, Beach Villas, 098269",
        "city": "Singapore",
        "country": "Singapore"
    },
    "description": "Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station.",
    "amenities": {
        "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
        "room": ["aircon", "tv", "coffee machine", "kettle", "hair dryer", "iron", "bathtub"]
    },
    "images": {
        "rooms": [
            { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg", "description": "Double room" },
            { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg", "description": "Double room" },
            { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg", "description": "Bathroom" }
        ],
        "site": [
            { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg", "description": "Front" }
        ],
        "amenities": [
            { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg", "description": "RWS" }
        ]
    },
    "booking_conditions": [
        "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
        "Pets are not allowed.",
        "WiFi is available in all areas and is free of charge."
    ]
}

hotel = Hotel(**data)
