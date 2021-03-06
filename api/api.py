from urllib import request
import json

base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"

class Api:
    def __init__(self):
        self.base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"
    
    def get_all(self, url, user_id, search, post_id):
        try:
            all_url = url + 'all.php'
            
            if user_id is not None:
                all_url += '?userId=' + str(user_id)
            if user_id is None and search is not None:
                all_url += '?search=' + search
            if post_id is not None:
                all_url += '?postId=' + str(post_id)
                
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