from abc import ABC, abstractmethod
from urllib import request
import json

base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"

class Api(ABC):
    def __init__(self):
        self.base_url = "http://localhost/ExpenseTrackerAPI-PHP/api/"
    
    def get_all(self, url, user_id):
        with request.urlopen(url) as all:
            serial_data = all.read()
            data = json.loads(serial_data)
        
        return data
    
    
    def create(self, url, **kargs):
        data = kargs
        self.json_encode(url, data=data)
        
        
    def json_encode(self, url, data):
        data = json.dumps(data)
        data = str(data)
        data = data.encode('utf-8')
        
        req = request.Request(url, data=data)
        
        request.urlopen(req)