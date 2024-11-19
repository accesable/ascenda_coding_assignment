from dataclasses import dataclass
import json
import argparse
from implemations import Acme,Paperflies,Patagonia
from intefaces import BaseSupplier
from models import Hotel
from typing import List, Dict
import requests
from suppliers import *
from hotelservice import *

def fetch_hotels(hotel_ids, destination_ids):
    
    # Register the supplier classes
    SupplierFactory.register_supplier(Acme)
    SupplierFactory.register_supplier(Paperflies)
    SupplierFactory.register_supplier(Patagonia) 
    
    # Fetch all suppliers from the factory
    suppliers = SupplierFactory.get_suppliers()

    # Inject suppliers into the service
    service = SupplierService(suppliers)

    # Get all hotels from all suppliers
    hotels = service.get_all_hotels()

    hotelService = HotelsServiceImpl()
    hotelService.merge_and_save(hotels)
    res = []
    if hotel_ids == 'none' and destination_ids == 'none' :
        for hotel in hotelService.hotels:
            res.append(hotel.to_dict())
    else :
        hotels_idlist = set()
        if hotel_ids != 'none' :
            for id in hotel_ids.split(','):
                hotels_idlist.add(str(id).strip())
        location_ids = set()
        if destination_ids != 'none':
            for location in destination_ids.split(','):
                location_ids.add(int(location))

        hotels = hotelService.find_hotel_by_id_and_location(hotels_idlist, location_ids)
        for hotel in hotels:
            res.append(hotel.to_dict())
            
    return json.dumps(res,indent=4)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("hotel_ids", type=str, help="Hotel IDs")
    parser.add_argument("destination_ids", type=str, help="Destination IDs")

    # Parse the arguments
    args = parser.parse_args()

    hotel_ids = args.hotel_ids
    destination_ids = args.destination_ids

    result = fetch_hotels(hotel_ids,destination_ids)
    print(result)
      

if __name__ == "__main__":
    main()