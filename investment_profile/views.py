from django.shortcuts import render
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from metadata.functions.metadata import getConfig, configureLogging
from metadata.functions.service import validateCookieService, getProfileQuestionsService
import json
from investment_profile.functions.investment_profile_service import saveInvestmentProfileService, getInvestmentProfileService


# Create your views here.


@csrf_exempt
@api_view(['GET'])
def investmentProfileQuestionsView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                response['statusCode'] = 5
                raise Exception("Authentication failure")
        else:
            response['statusCode'] = 5
            raise Exception("Authentication failure")
               
       
        if request.method == "GET":
            #print(request.POST)
            profileQuestions=getProfileQuestionsService('I')
            #print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = profileQuestions
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving Investment Profile questions'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['POST','GET'])
def InvestmentProfileView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
       
        
        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                response['statusCode'] = 5
                raise Exception("Authentication failure")
        else:
            response['statusCode'] = 5
            raise Exception("Authentication failure")
        
        
        if request.method == "POST":
            saveInvestmentProfileService(json.loads(request.body.decode('utf-8')),request.COOKIES['userName'])
            response['statusCode'] = 0
            response['data'] = 'Investment Profile data saved successfully'
        elif request.method == "GET":
            investmentProfielList = getInvestmentProfileService(request.COOKIES['userName'])
            response['statusCode'] = 0
            response['data'] = investmentProfielList
                
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in processing Investment Profile data'
        response['error'] = str(e)
    return JsonResponse(response)


