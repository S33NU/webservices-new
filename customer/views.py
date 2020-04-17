from django.shortcuts import render
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from metadata.functions.metadata import getConfig, configureLogging
from metadata.functions.service import validateCookieService
import json
# Create your views here.
from customer.functions.customer_service import getCustomerEmailandMobileService


@csrf_exempt
@api_view(['GET'])
def getEmailandMobile(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)
        
        cookieVal= ''
        try:
            cookieVal=validateCookieService(request)    
        except Exception as e:
            if str(e) == "Authentication failure":
                response['statusCode'] = 5
            raise 
        
        if request.method == "GET":
            data=getCustomerEmailandMobileService(cookieVal)
            response['statusCode'] = 0
            response['data'] = data
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retreiving registration details'
        response['error'] = str(e)
    return JsonResponse(response)



