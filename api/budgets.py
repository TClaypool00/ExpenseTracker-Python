from api.api import base_url, Api

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