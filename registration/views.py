from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging,get_client_ip
import logging
import json
from rest_framework.decorators import api_view
from registration.functions.registration_service import saveClientPasswordService, checkClientPasswordService,saveClientMobileService, validateMobileandSaveService , validateClientPasswordService, verifyOTPService
from metadata.functions.service import validateCookieService, verifyOTPByEmailService
from registration.functions.registration_service import checkClientPasswordByEmailService, validateEmailandSaveService,validateClientPasswordByEmailService 

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

        
        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                response['statusCode'] = 5
                raise Exception("Authentication failure")
        else:
            response['statusCode'] = 5
            raise Exception("Authentication failure")
            
        
        if request.method == "PUT":
            #print(json.loads(request.body.decode('utf-8')))
            saveClientPasswordService(json.loads(request.body.decode('utf-8')))
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
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
        config = getConfig()
        log = config['log']
        configureLogging(log)
        if request.method == "POST":
            ip = get_client_ip(request)
            device = request.META['HTTP_USER_AGENT']
           
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
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
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
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
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
def checkPassword(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            if checkClientPasswordService(json.loads(request.body.decode('utf-8'))):
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = True
            else:
                response['statusCode'] = 0
                response['data'] = False
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in checking client password'
        response['error'] = str(e)
    return JsonResponse(response)





@csrf_exempt
@api_view(['POST'])
def validateEmail(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
        config = getConfig()
        log = config['log']
        configureLogging(log)
        if request.method == "POST":
            ip = get_client_ip(request)
            device = request.META['HTTP_USER_AGENT']
           
            hasNoClientDetails = validateEmailandSaveService(json.loads(request.body.decode('utf-8')), ip, device)
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
        response['data'] = 'Error in validating client email'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['POST'])
def validateClientByEmail(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            if validateClientPasswordByEmailService(json.loads(request.body.decode('utf-8'))):
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = 'Client credentials successfully validated'
            else:
                response['statusCode'] = 2
                response['data'] = 'Invalid client credentials'
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in validting client credentials by email '
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['POST'])
def verifyOTPBByEmail(request):
    
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
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
def checkPasswordByEmail(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        '''
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")
        '''
        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":
            if checkClientPasswordByEmailService(json.loads(request.body.decode('utf-8'))):
                # print(json.loads(request.body.decode('utf-8')))
                response['statusCode'] = 0
                response['data'] = True
            else:
                response['statusCode'] = 0
                response['data'] = False
                    
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in checking client password'
        response['error'] = str(e)
    return JsonResponse(response)








