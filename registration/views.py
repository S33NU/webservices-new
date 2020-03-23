from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
import logging
import json
from rest_framework.decorators import api_view
from registration.functions.registration_service import saveClientPasswordService, saveClientMobileService


@csrf_exempt
@api_view(['PUT', 'POST'])
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
        try:
            if request.method == "POST":
                print(json.loads(request.body.decode('utf-8')))
                saveClientMobileService(json.loads(request.body.decode('utf-8')))
                response['data'] = 'Client Mobile number saved successfully'
                response['statusCode'] = 0
        except Exception:
            response['data'] = True
            response['error'] = 'null'
            response['statusCode'] = 0




    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving client details '
        response['error'] = str(e)
    return JsonResponse(response)
