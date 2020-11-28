from .api import base_url, Api
from urllib import request
import json

posts_url = base_url + 'posts/'

create_url = posts_url + 'create.php'

post_id = posts_url + 'get.php?postId='

class PostsApi(Api):
    def create_post(self, title, post_body, user_id):
        data = {'title' : title, 'postBody' : post_body, 'userId' : user_id}
        self.json_encode(Api, create_url, data=data)
        
    
    def post_by_id(self, id):
        try:
            url = post_id + str(id)
        
            with request.urlopen(url) as all:
                    serial_data = all.read()
                    data = json.loads(serial_data)
            return data
        except Exception:
            return None