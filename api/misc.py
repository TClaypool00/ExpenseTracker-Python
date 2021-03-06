from urllib import request
from .api import base_url
import json
from api.api import Api

misc_url = base_url + 'misc/'

class MiscApi(Api):
    def create_misc(self,price, store_id, user_id, memo, misc_name):
        url = misc_url + 'create.php'
        data = {'price' : price, 'storeId' : store_id, 'userId' : user_id, 'memo': memo, 'miscName' : misc_name}
        self.json_encode(self, url, data=data)
        
    
    def get_misc_by_id(self, misc_id):
        url = misc_url + 'get.php?miscId=' + str(misc_id)
        
        return self.read_data(Api, url)