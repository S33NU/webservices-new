from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
import logging
from metadata.functions.metadata import getConfig, configureLogging
from metadata.functions.service import validateCookieService

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request,"index.html")  
@csrf_exempt
def savePassword(request,phonenumber):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                raise Exception("Authentication failure")
        
       
        if request.method == 'GET':   
            return render(request,"password.html",{'phonenumber':phonenumber})
        
    except Exception as e:
        logging.error(str(e))
        return render(request,"error.html",{'redirectLink':'../login'})

@csrf_exempt
def emailLogin(request):
    if request.method == 'GET':
        return render(request,"emaillogin.html")  

@csrf_exempt
def personalProfile(request):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)
        
        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                raise Exception("Authentication failure")
        
        if request.method == 'GET':   
            return render(request,"personalProfile.html")  
        
        
    except Exception as e:
        logging.error(str(e))
        return render(request,"error.html",{'redirectLink':'login'})



