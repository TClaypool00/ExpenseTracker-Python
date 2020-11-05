from urllib import request
from .api import base_url
import json
from api.users import UserApi

store_url = base_url + 'store-union/'

class StoreApi(UserApi):
    def get_all_stores(self, is_credit_union):
        all_url = store_url + 'all.php?isUnion='
        if is_credit_union == False:
            url = all_url + '0'
        else:
            url = all_url + '1'
        
        with request.urlopen(url) as all:
            serial_data = all.read()
            return json.loads(serial_data)