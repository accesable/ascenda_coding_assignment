# Assignment Result
## Overview
The Objective of the assignment is to group and merge data from multiple suppliers. 
## Design Patterns Applied
- Factory Methods for creating and registering many implementations of the suppliers abstract
```python
class BaseSupplier:
    def endpoint():
        """URL to fetch supplier data"""
        pass

    def parse(obj: dict) -> Hotel:
        pass

    def fetch(self):
        url = self.endpoint()
        resp = requests.get(url).json()
        return [self.parse(dto) for dto in resp]
```
```python
class SupplierFactory:
    _supplier_classes = []

    @staticmethod
    def register_supplier(supplier_cls):
        SupplierFactory._supplier_classes.append(supplier_cls)

    @staticmethod
    def get_suppliers() -> List[BaseSupplier]:
        return [supplier_cls() for supplier_cls in SupplierFactory._supplier_classes]


class SupplierService:
    def __init__(self, suppliers: List[BaseSupplier]):
        self.suppliers = suppliers

    def get_all_hotels(self) -> List[Hotel]:
        hotels = []
        for supplier in self.suppliers:
            hotels.extend(supplier.fetch())
        return hotels
```
- If there more supplier implementations the mergering algorithm is modified. So I implemented the strategy pattern 
```python
class MergeHotelStrategy():
    def merge(self,obj1,obj2):
        pass

class MergeContext:
    def __init__(self, strategy: MergeHotelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: MergeHotelStrategy):
        self.strategy = strategy

    def merge(self, item1, item2):
        return self.strategy.merge(item1, item2)
        
```
The logic of merge is that I prioritize the suppliers data fields with order. For example, Acme -> Paperfiles -> Patogonia so i will have 2 merge strategies implemented from `MergeHotelStrategy` From Acme -> Paperfiles and Paperfiles -> Patogonia. The Algorithms is based on the suppliers to decide which strategy to use
test
```bash
# cd to src
cd src
python hotel_merger.py f8c9,iJhz none
python hotel_merger.py none 5432
python hotel_merger.py none 5432,1122
python hotel_merger.py none none
```