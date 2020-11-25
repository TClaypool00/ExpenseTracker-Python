from django.shortcuts import render

def community_index(request):
    return render(request, 'community_index.html')