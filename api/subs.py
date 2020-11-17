from urllib import request
from .api import base_url
import json
from api.api import Api

sub_url =  base_url + 'subs/'

class SubsApi(Api):
    def create_sub(self, due_date, amt_due, store_id, sub_name, user_id):
        url = sub_url + 'create.php'
        data = {'dueDate' : due_date, 'amountDue' : str(amt_due), 'storeId' :store_id, 'subName' : sub_name, 'userId' : str(user_id)}
        self.json_encode(self, url, data=data)
        
    
    def get_sub_by_id(self, sub_id):
        url = sub_url + 'get.php?subId=' + str(sub_id)
        
        return self.read_data(Api, url)