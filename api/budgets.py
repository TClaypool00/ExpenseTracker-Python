from api.api import base_url, Api
from urllib import request
import json

budget_url = base_url + 'budgets/'

class BudgetApi:
    def create_budget(self, user_id):
        url = budget_url + 'create.php'
        data = {'userId' :user_id}
        Api.json_encode(self, url, data=data)
        
        
    def update_budget(self, user_id, savings_money, budget_id):
        url = budget_url + 'update.php?budgetId=' + str(budget_id)
        data = {'userId' : user_id, 'savingsMoney' : savings_money}
        Api.json_encode(self, url, data=data)
        
    
    def get(self, user_id, budget_id):
        url = budget_url + 'get.php?'
        if budget_id == None:
            url = url + 'userId=' + str(user_id)
        else:
            url = url + 'budgetId=' + str(budget_id)
        
        try:
            with request.urlopen(url) as all:
                serial_data = all.read()
                data = json.loads(serial_data)
            
            return data
        except Exception:
            return None