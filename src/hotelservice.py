from models import Hotel
from typing import List,Dict,Set,Tuple
from mergering import *
import heapq
from collections import defaultdict
class HotelsService():
    
    def __init__(self) -> None:
        self.priorities = {
            'Acme': 1,
            'Paperflies': 2,
            'Patagonia': 3,
        }
        self.hotels = []
    
    def merge_and_save(self,hotels : List[Hotel]) -> List[Hotel]:
        pass
    
    def find_hotel_by_id_and_location(self, id : str, location :int) -> List[Hotel]:
        pass

class HotelsServiceImpl(HotelsService):
    def merge_and_save(self, hotels : List[Hotel]) -> None:
        duplicated_indices : Dict[str,List[Tuple[int,int]]] = defaultdict(list)
        for i in range(len(hotels)):
            hotel_id = hotels[i].id
            if hotel_id in duplicated_indices:
                heapq.heappush(duplicated_indices[hotel_id],(self.priorities[hotels[i].supplier_name],i))
            else:
                heapq.heappush(duplicated_indices[hotel_id],(self.priorities[hotels[i].supplier_name],i))
        
        
        data = []
        
        for duplicated_i in duplicated_indices.values():
            mergeContext = MergeContext(MergeHotelAcmeToPaperfiles())
            for i in range(len(duplicated_i)-1):
                cur_hotel_i = duplicated_i[i][1]
                next_hotel_i = duplicated_i[i+1][1]
                cur_hotel = hotels[cur_hotel_i]
                next_hotel = hotels[next_hotel_i]
                merged_item = mergeContext.merge(cur_hotel,next_hotel)
                if duplicated_i[i+1][0] == 2:
                    mergeContext.set_strategy(MergeHotelPaperfilesToPatagonia())
                hotels[next_hotel_i] = merged_item
                
            data.append(merged_item)
        
        self.hotels = data
    
    def find_hotel_by_id_and_location(self, id : List[str], location : Set[int]) -> List[Hotel]:
        res = [] 
        for i in self.hotels :
            if i.id in id or i.destination_id in location :
                res.append(i)
                
        return res
        