from urllib import request
from .api import base_url
import json

bill_url = base_url + "bills/"

class BillsApi:
    def get_all_bills_by_user_id(self, user_id):
        with request.urlopen(bill_url + "all.php?userId=" + str(user_id)) as all:
            serial_data = all.read()
            data = json.loads(serial_data)
        
        return data
    
    
    def create_bill(self, bill_name, bill_date, bill_price, is_late, store_id, user_id):
        url = bill_url + 'create.php'
        data = {'billName': bill_name, 'billDate': bill_date, 'billPrice' : bill_price, 'isLate' : is_late, 'storeId' : store_id, 'userId' : user_id}
        data = json.dumps(data)
        data = str(data)
        data = data.encode("utf-8")

        req = request.Request(url, data=data)

        request.urlopen(req)