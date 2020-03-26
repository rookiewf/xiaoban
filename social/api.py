from django.http import JsonResponse
from django.shortcuts import render
from social import logics

# Create your views here.
def get_rcmd_users(request):
    users = logics.rcmd_users(request.user)
    print(users)
    res = [user.to_dict() for user in users]
    return JsonResponse({'code':'1000','data':res})
