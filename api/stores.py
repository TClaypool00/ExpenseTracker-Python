from urllib import request
from .api import base_url
import json
from api.users import UserApi

store_url = base_url + 'store-union/'

class StoreApi(UserApi):
    def get_all_stores(self):
        with request.urlopen(store_url + 'all.php') as all:
            serial_data = all.read()
            data = json.loads(serial_data)
            
        return data