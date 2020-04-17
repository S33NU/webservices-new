from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging,get_client_ip
import logging
import json
from rest_framework.decorators import api_view
from registration.functions.registration_service import saveClientPasswordService,saveClientMobileService, validateMobileandSaveService , validateClientPasswordService, verifyOTPService
from metadata.functions.service import validateCookieService
from registration.functions.registration_service import resendOTPService,sendOTPByEmailService,verifyOTPByEmailService 

@csrf_exempt
@api_view(['PUT'])
def savePassword(request):
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
               
        if request.method == "PUT":
            #print(json.loads(request.body.decode('utf-8')))
            saveClientPasswordService(json.loads(request.body.decode('utf-8')),cookieVal)
            # print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = 'Client password saved successfully'
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving client password'
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['POST'])
def validatePhoneno(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        
        config = getConfig()
        log = config['log']
        configureLogging(log)
        if request.method == "POST":
            ip = get_client_ip(request)
            device = request.user_agent.device.family
            
            hasNoClientDetails = validateMobileandSaveService(json.loads(request.body.decode('utf-8')), ip, device)
            if hasNoClientDetails == True:
                #print(json.loads(request.body.decode('utf-8')))
                
                
                response['data'] = False
                response['error'] = 'null'
                response['statusCode'] = 0
            else:
                response['data'] = True
                response['error'] = 'null'
                response['statusCode'] = 0
                
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in validating client phone number'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['POST'])
def validateClient(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
       
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            if validateClientPasswordService(json.loads(request.body.decode('utf-8'))):
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = 'Client credentials successfully validated'
            else:
                response['statusCode'] = 2
                response['data'] = 'Invalid client credentials'
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in validting client credentials '
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['POST'])
def verifyOTP(request):
    
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            otpStatus = verifyOTPService(json.loads(request.body.decode('utf-8')))
            
            if otpStatus == True:
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = 'OTP successfully verified'
            else:
                response['statusCode'] = 3
                response['data'] = 'Invalid OTP'
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in validting client credentials '
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['POST'])
def verifyOTPByEmail(request):
    
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            otpStatus = verifyOTPByEmailService(json.loads(request.body.decode('utf-8')))
            
            if otpStatus == True:
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = 'OTP successfully verified'
            else:
                response['statusCode'] = 3
                response['data'] = 'Invalid OTP'
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in validting client credentials '
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['POST'])
def sendOTPByEmail(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            sendOTPByEmailService(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = "OTP Successfully sent to email"
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in sending OTP to email'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['POST'])
def resendOTP(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            resendOTPService(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = "OTP Successfully sent again"
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in resending OTP'
        response['error'] = str(e)
    return JsonResponse(response)






