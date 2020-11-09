from urllib import request

from django.http.response import Http404
from .api import base_url
import json

loan_url = base_url + 'loan/'

class LoanApi:
    def get_loan_by_user_id(self, user_id):
        try:
            with request.urlopen(loan_url + 'all.php?userId=' + str(user_id)) as all:
                serial_data = all.read()
                data = json.loads(serial_data)
            
            return data
        except Exception:
            return None
    
    
    def create_loan(self, loan_name, due_date, monthly_amt_due, deposit, total_amt_due, store_id, user_id):
        url = loan_url + 'create.php'
        data = {'loanName' : loan_name, 'dueDate' : due_date, 'monthlyAmountDue' : monthly_amt_due, 'deposit' : deposit, 'totalAmountDue' : total_amt_due, 'storeId' : store_id, 'userId' : user_id}
        self.__json_encode(self, url, data)
        
    
    
    def __json_encode(self, url, data):
        data = json.dumps(data)
        data = str(data)
        data = data.encode('utf-8')
        
        req = request.Request(url, data=data)
        
        request.urlopen(req)