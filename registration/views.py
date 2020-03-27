from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging,get_client_ip
import logging
import json
from rest_framework.decorators import api_view
from registration.functions.registration_service import saveClientPasswordService, saveClientMobileService, validateMobileandSaveService , validateClientPasswordService, verifyOTPService



@csrf_exempt
@api_view(['PUT'])
def savePassword(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    try:
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")

        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "PUT":
            print(json.loads(request.body.decode('utf-8')))
            saveClientPasswordService(json.loads(request.body.decode('utf-8')))
            # print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = 'Client password saved successfully'
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving client details '
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
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")

        config = getConfig()
        log = config['log']
        configureLogging(log)
        if request.method == "POST":
            ip = get_client_ip(request)
            device = request.META['HTTP_USER_AGENT']
            print(type(ip))
            print(ip, device)
            hasNoClientDetails = validateMobileandSaveService(json.loads(request.body.decode('utf-8')), ip, device)
            if hasNoClientDetails == True:
                print(json.loads(request.body.decode('utf-8')))
                saveClientMobileService(json.loads(request.body.decode('utf-8')), ip, device)
                response['data'] = False
                response['error'] = 'null'
                response['statusCode'] = 0
            else:
                response['data'] = True
                response['error'] = 'null'
                response['statusCode'] = 0
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving client details '
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
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")

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
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")

        config = getConfig()
        log = config['log']
        configureLogging(log)

        if request.method == "POST":

            if verifyOTPService(json.loads(request.body.decode('utf-8'))):
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


