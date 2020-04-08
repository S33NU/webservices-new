from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
import logging
from metadata.functions.metadata import getConfig, configureLogging, getCurrentPath
from metadata.functions.service import validateCookieService
from rest_framework.decorators import api_view
import sys

            
from investment_profile.functions.investment_profile_service import getInvestmentProfileQuestionsService
from customer.functions.customer_service import getCustomerDetailsService
from metadata.functions.service import getMenuItemsByCustomerStatuService
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
            customerDetailsObj=getCustomerDetailsService(request.COOKIES['userName'])
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus) 
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"password.html","menuItemList":menuItemList})  
            else:
                raise Exception("Access Denied")    
        
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            errorMessage = "Access Denied. Please Login"
            redirectLink ="../login"
        elif str(e) == "Access Denied":
            errorMessage = "Access Denied. Go back to home page"
            redirectLink ="default"
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False               
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})

@csrf_exempt
@api_view(['GET'])
def personalProfile(request):
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
        if str(e) == "Authentication failure":
            errorMessage = "Access Denied. Please Login"
            redirectLink ="../login"
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False               
        
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})



@csrf_exempt
@api_view(['GET'])
def investmentProfile(request):
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
            investmentProfileQuestions=getInvestmentProfileQuestionsService()
            customerDetailsObj=getCustomerDetailsService(request.COOKIES['userName'])
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus) 
            
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"investmentProfile.html","investmentProfileQuestions":investmentProfileQuestions,'menuItemList':menuItemList})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            errorMessage = "Access Denied. Please Login"
            redirectLink ="../login"
        elif str(e) == "Access Denied":
            errorMessage = "Access Denied. Go back to home page"
            redirectLink ="default"
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
                           
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})






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
        if str(e) == "Authentication failure":
            errorMessage = "Access Denied. Please Login"
            redirectLink ="../login"
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False               
        
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})


