from django.shortcuts import render
from api.users import UserApi

def index(request):
    data = UserApi.get_all(request)
    return render(request, 'user-index.html', {"users": data})