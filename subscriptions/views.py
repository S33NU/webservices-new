from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
from subscriptions.functions.subscriptions_service import getSubscriptionsService, saveSubscriptionService,reviewInvestmentService,saveDocumentsService
import logging
import json
from rest_framework.decorators import api_view
from metadata.functions.service import validateCookieService

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def subscriptionsView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        cookieVal= ''
        try:
            cookieVal=validateCookieService(request)    
        except Exception as e:
            if str(e) == "Authentication failure":
                response['statusCode'] = 5
            raise       
                 
        if request.method == "GET":
            subscriptionList = getSubscriptionsService()
            response['statusCode'] = 0
            response['data'] = subscriptionList
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving subscription data'
        response['error'] = str(e)
    return JsonResponse(response)      


@csrf_exempt
@api_view(['POST'])
def subscriptionCompleted(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        cookieVal= ''
        try:
            cookieVal=validateCookieService(request)    
        except Exception as e:
            if str(e) == "Authentication failure":
                response['statusCode'] = 5
            raise       
                 
        if request.method == "POST":
            subscriptionList = saveSubscriptionService(json.loads(request.body.decode('utf-8')),cookieVal)
            response['statusCode'] = 0
            response['data'] = subscriptionList
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving subscription data'
        response['error'] = str(e)
    return JsonResponse(response)   


@csrf_exempt
@api_view(['POST'])
def reviewInvestment(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        cookieVal= ''
        try:
            cookieVal=validateCookieService(request)    
        except Exception as e:
            if str(e) == "Authentication failure":
                response['statusCode'] = 5
            raise       
                 
        if request.method == "POST":
            subscriptionList = reviewInvestmentService(cookieVal)
            response['statusCode'] = 0
            response['data'] = subscriptionList
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving subscription data'
        response['error'] = str(e)
    return JsonResponse(response)   

@csrf_exempt
@api_view(['POST'])
def submitDocuments(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        cookieVal= ''
        try:
            cookieVal=validateCookieService(request)    
        except Exception as e:
            if str(e) == "Authentication failure":
                response['statusCode'] = 5
            raise       
                 
        if request.method == "POST":
            subscriptionList = saveDocumentsService(cookieVal)
            response['statusCode'] = 0
            response['data'] = subscriptionList
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving subscription data'
        response['error'] = str(e)
    return JsonResponse(response)   
