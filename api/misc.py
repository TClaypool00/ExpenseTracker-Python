from urllib import request
from .api import base_url
import json
from api.api import Api

misc_url = base_url + 'misc/'

class MiscApi(Api):
    def create_misc(self,price, store_id, date, user_id, memo, misc_name):
        url = misc_url + 'create.php'
        data = {'price' : price, 'storeId' : store_id, 'date' : date, 'userId' : user_id, 'memo': memo, 'miscname' : misc_name}
        self.json_encode(self, url, data=data)