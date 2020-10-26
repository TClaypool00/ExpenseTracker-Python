from django.shortcuts import render
from api.users import UserApi
from django.contrib.auth.decorators import login_required
@login_required()
def index(request):
    data = UserApi.get_all(request)
    return render(request, 'user-index.html', {"users": data})