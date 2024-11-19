from models import *

class MergeHotelStrategy():
    def merge(self,obj1,obj2):
        pass
    
class MergeHotelAcmeToPaperfiles(MergeHotelStrategy):
    def merge(self,acme : Hotel,paperfiles : Hotel) -> Hotel:
        acme.description = paperfiles.description
        acme.amenities.general = paperfiles.amenities.general.copy()
        acme.amenities.room = paperfiles.amenities.room.copy()
        acme.booking_conditions = paperfiles.booking_conditions
        acme.images.rooms.extend(paperfiles.images.rooms)
        acme.images.site.extend(paperfiles.images.site)
        return acme

class MergeHotelPaperfilesToPatagonia(MergeHotelStrategy):
    def merge(self, paperfiles : Hotel, patagonia : Hotel) -> Hotel:
        if len(paperfiles.description) < len(patagonia.description):
            paperfiles.description = patagonia.description
        paperfiles.images.amenities = patagonia.images.amenities
        paperfiles.images.rooms.extend(patagonia.images.rooms)
        paperfiles.location.lat = patagonia.location.lat
        paperfiles.location.lng = patagonia.location.lng
        
        return paperfiles
    
class MergeContext:
    def __init__(self, strategy: MergeHotelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: MergeHotelStrategy):
        self.strategy = strategy

    def merge(self, item1, item2):
        return self.strategy.merge(item1, item2)
        