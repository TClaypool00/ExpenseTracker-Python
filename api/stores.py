from urllib import request
from .api import base_url
import json
from api.api import Api

store_url = base_url + 'store-union/'

class StoreApi(Api):
    def get_all_stores(self, is_credit_union):
        all_url = store_url + 'all.php?isUnion='
        if is_credit_union == False:
            url = all_url + '0'
        else:
            url = all_url + '1'
        
        try:
            with request.urlopen(url) as all:
                serial_data = all.read()
                return json.loads(serial_data)
        except Exception:
            return None
        
    
    def create_store(self, store_name, address, city, state, zip, phone_num, email, website, is_credit_union):
        url = store_url + 'create.php'
        data = {'storeName' : store_name, 'address' : address, 'city' : city, 'state' : state, 'zip' : zip, 'phoneNum' : phone_num, 'email' : email, 'website': website, 'isCreditUnion': is_credit_union}
        self.json_encode(self, url, data=data)