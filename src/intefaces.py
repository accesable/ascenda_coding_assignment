from models import Hotel
import requests
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