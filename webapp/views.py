from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
import logging
from metadata.functions.metadata import getConfig, configureLogging, getCurrentPath
from metadata.functions.service import validateCookieService
from rest_framework.decorators import api_view
import sys

            
from investment_profile.functions.investment_profile_service import getInvestmentProfileQuestionsService
from personal_profile.functions.personal_profile_service import getPersonalProfileQuestionsService
from customer.functions.customer_service import getCustomerDetailsService,updateCustomerDetailsService
from metadata.functions.service import getMenuItemsByCustomerStatuService,checkSubscriptionExpirationService


# Create your views here.

@csrf_exempt
@api_view(['GET'])
def login(request):
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if 'userName' in request.COOKIES:
            if validateCookieService(request.COOKIES['userName']):
                raise Exception('Logged In')
       
        if request.method == 'GET':
            return render(request,"index.html")  
        
        
    except Exception as e:
        logging.error(str(e))
        return redirect('home/default')    
    
    
    


@csrf_exempt
@api_view(['GET'])
def savePasswordPage(request):
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
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"password.html","menuItemList":menuItemList})  
            else:
                raise Exception("Access Denied")    
        
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False               
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})

@csrf_exempt
@api_view(['GET'])
def personalProfilePage(request):
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
            personalProfileQuestions = getPersonalProfileQuestionsService()
            customerDetailsObj=getCustomerDetailsService(request.COOKIES['userName'])
            
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"personalProfile.html","personalProfileQuestions":personalProfileQuestions,'menuItemList':menuItemList})
            else:
                raise Exception("Access Denied")    
            
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
                           
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})



@csrf_exempt
@api_view(['GET'])
def investmentProfilePage(request):
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
            
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"investmentProfile.html","investmentProfileQuestions":investmentProfileQuestions,'menuItemList':menuItemList})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
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
            
            
            
            customerDetailsObj=getCustomerDetailsService(request.COOKIES['userName'])
            
            if customerDetailsObj.customerStatus_new in "S,I" and not checkSubscriptionExpirationService(request.COOKIES['userName']):
                updateCustomerDetailsService({'username':request.COOKIES['userName'],'customerStatus':'E'})
                return redirect('../home/default')
            
            
            
            if customerDetailsObj.customerStatus_new == 'P':
                return redirect('../home/save-password')    
            elif customerDetailsObj.customerStatus_new == 'R':
                return redirect('../home/subscription')    
            elif customerDetailsObj.customerStatus_new == 'S':
                return redirect('../home/dashboard')    
            elif customerDetailsObj.customerStatus_new == 'I':
                return redirect('../home/invested')    
            elif customerDetailsObj.customerStatus_new == 'E':
                return redirect('../home/subscription')    
            
            #return render(request,"home.html",{"template_name":"personalProfile.html"})  
            #return render(request,"home.html",{"template_name":"dashboardview1.html"})  
           
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False               
            return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})

@csrf_exempt
@api_view(['GET'])
def subscriptionPage(request):
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
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"subscription.html",'menuItemList':menuItemList})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})


@csrf_exempt
@api_view(['GET'])
def documentPage(request):
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
            
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"documents.html",'menuItemList':menuItemList})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})


@csrf_exempt
@api_view(['GET'])
def dashboardPage(request):
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
            profileLink = ''
            profileCompleted = False
            if 'personal' in customerDetailsObj.profileStatus:
                profileLink = 'personal-profile'
                profileCompleted = False
            elif 'invest' in customerDetailsObj.profileStatus:
                profileLink =  'investment-profile'
                profileCompleted = False
            elif 'document' in customerDetailsObj.profileStatus:
                profileLink = 'documents'
                profileCompleted = False
            else:
                profileCompleted = True    
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"dashboardview1.html",'menuItemList':menuItemList,'profileLink':profileLink,'profileCompleted':profileCompleted})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})



@csrf_exempt
@api_view(['GET'])
def investedPage(request):
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
            if customerDetailsObj.customerStatus_new in "S,I" and not checkSubscriptionExpirationService(request.COOKIES['userName']):
                updateCustomerDetailsService({'username':request.COOKIES['userName'],'customerStatus':'E'})
                return redirect('../home/default')
            
            
            menuItemList=getMenuItemsByCustomerStatuService(customerDetailsObj.customerStatus_new) 
            
            currentPath=getCurrentPath(request.path)
            menuItemObjList = [child for menuItemObj in menuItemList for child in menuItemObj['child'] if child['menuItemLink'] == currentPath ]
            if len(menuItemObjList) == 1:
                return render(request,"home.html",{"template_name":"dashboardview2.html",'menuItemList':menuItemList})  
            else:
                raise Exception("Access Denied")    
        
    except Exception as e:
        logging.error(str(e))
        if str(e) == "Authentication failure":
            return redirect('/ui/login')
        elif str(e) == "Access Denied":
            return redirect('../home/default')
        else:
            errorMessage = "Internal Server Error"
            redirectLink = False
        return render(request,"error.html",{'redirectLink':redirectLink,'errorMessage':errorMessage})




