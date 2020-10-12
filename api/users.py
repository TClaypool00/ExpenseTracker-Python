from urllib import request
from .api import base_url
import json

user_url = base_url + "users/"

class UserApi:
    def get_all(self):
        with request.urlopen(user_url + "all.php") as all:
            serial_data = all.read()
            data = json.loads(serial_data)
        
        return data
    
    def create_user(self, first_name, last_name, email, password, is_admin, phone_num, salary):
        url = user_url + "create.php"

        data = {"firstName" : first_name, "lastName" : last_name, "email" : email, "password" : password, "isAdmin" : is_admin, "phoneNum": phone_num, "salary": salary}

        data = json.dumps(data)
        data = str(data)
        data = data.encode("utf-8")

        req = request.Request(url, data=data)

        request.urlopen(req)
        
    def user_by_id(self, id):
        with request.urlopen(user_url + "get.php?userId=" + id) as user:
            serial_data = user.read()
            data = json.loads(serial_data)
            
        return data