from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request,"index.html")  
@csrf_exempt
def savePassword(request):
    if request.method == 'GET':
        return render(request,"password.html")  
@csrf_exempt
def emailLogin(request):
    if request.method == 'GET':
        return render(request,"emaillogin.html")  

@csrf_exempt
def personalProfile(request):
    if request.method == 'GET':
        return render(request,"personalProfile.html")  




