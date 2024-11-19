from intefaces import BaseSupplier
from typing import List
from models import Hotel

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
