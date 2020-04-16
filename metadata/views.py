from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
import logging
from metadata.functions.metadata import getConfig, configureLogging
from metadata.functions.service import getCountryCodesService
from rest_framework.decorators import api_view
import sys


@csrf_exempt
@api_view(['GET'])
def getCountryCodes(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
       
        
        if request.method == "GET":
            countreyCodesList = getCountryCodesService()
            response['data'] = countreyCodesList
            response['statusCode'] = 0
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retreving country codes data'
        response['error'] = str(e)
    return JsonResponse(response)