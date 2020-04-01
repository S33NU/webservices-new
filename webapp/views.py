from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
import logging
from metadata.functions.metadata import getConfig, configureLogging
from metadata.functions.service import validateCookieService
from rest_framework.decorators import api_view
import sys
# Create your views here.

@csrf_exempt
@api_view(['GET'])
def login(request):
    if request.method == 'GET':
        return render(request,"index.html")  


@csrf_exempt
@api_view(['GET'])
def savePassword(request):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                raise Exception("Authentication failure")
        else:
            raise Exception("Authentication failure")
        
       
        if request.method == 'GET':   
            return render(request,"home.html",{"template_name":"password.html"})  
        
        
    except Exception as e:
        logging.error(str(e))
        return render(request,"error.html",{'redirectLink':'../login'})

@csrf_exempt
@api_view(['GET'])
def emailLogin(request):
    if request.method == 'GET':
        return render(request,"emaillogin.html")  

@csrf_exempt
@api_view(['GET'])
def personalProfile(request):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)
        
        if 'userName' in request.COOKIES:
            print(request.COOKIES)
            if not validateCookieService(request.COOKIES['userName']):
                raise Exception("Authentication failure")
        else:
            raise Exception("Authentication failure")
        
        if request.method == 'GET':   
            return render(request,"home.html",{"template_name":"personalProfile.html"})  

        
    except Exception as e:
        logging.error(str(e))
        return render(request,"error.html",{'redirectLink':'../login'})




@csrf_exempt
@api_view(['GET'])
def homePage(request):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)
        
        if 'userName' in request.COOKIES:
            
            if not validateCookieService(request.COOKIES['userName']):
                raise Exception("Authentication failure")
        else:
            raise Exception("Authentication failure")
        
        if request.method == 'GET':  
            return render(request,"home.html",{"template_name":"personalProfile.html"})  
        
        
    except Exception as e:
        logging.error(str(e))
        return render(request,"error.html",{'redirectLink':'../login'})


