from urllib import request
import json

base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"

class Api:
    def __init__(self):
        self.base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"
    
    def get_all(self, url, search, user_id):
        all_url = url + 'all.php'
        try:
            if user_id is None:
                if search is None:
                    all_url
                else:
                    all_url + '?search=' + search
            else:
                all_url + '?userId=' + str(user_id)
            with request.urlopen(all_url) as all:
                serial_data = all.read()
                data = json.loads(serial_data)
            
            return data
        except Exception:
            return None
    
    
    def create(self, url, **kargs):
        data = kargs
        self.json_encode(url, data=data)
        
        
    def json_encode(self, url, data):
        data = json.dumps(data)
        data = str(data)
        data = data.encode('utf-8')
        
        req = request.Request(url, data=data)
        
        request.urlopen(req)
        
    def read_data(self, url):
        try:
            with request.urlopen(url) as all:
                serial_data = all.read()
                data = json.loads(serial_data)
            
            return data
        except Exception:
            return None