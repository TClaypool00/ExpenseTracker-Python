from .api import base_url, Api

posts_url = base_url + 'posts/'

create_url = posts_url + 'create.php'

class PostsApi(Api):
    def create_post(self, title, post_body, user_id):
        data = {'title' : title, 'postBody' : post_body, 'userId' : user_id}
        self.json_encode(Api, create_url, data=data)