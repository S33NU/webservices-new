from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
from personal_profile.functions.personal_profile_service import savePersonalProfileService,getPersonalProfileQuestionsService,personalProfileDataService,personalProfileDataByIdService,personalProfileEditDataByIdService
import logging
import json
from rest_framework.decorators import api_view
from personal_profile.functions.database import getProfileData
from metadata.functions.service import validateCookieService

@csrf_exempt
@api_view(['GET', 'POST'])
def personalProfileView(request):
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
            #print(request.POST)
            #print(json.loads(request.body))
            savePersonalProfileService(json.loads(request.body.decode('utf-8')),request.COOKIES['userName'])
            response['statusCode'] = 0
            response['data'] = 'Personal Profile data saved successfully'
        elif request.method == "GET":
            all_profiles = personalProfileDataService()
            response['data'] = all_profiles
            response['statusCode'] = 0
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving Personal Profile data'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['GET','PUT'])
def getprofilebyid(request, id):
    response = {
        'data': None,
        'error': None,
        'statusCode': None
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
            try:
                id = int(id)
            except:
                raise Exception("Profile ID must be a Number(Integer)")

            if id <= 0:
                raise Exception("Profile ID must be a Positive number and must be Existed")
            else:
                if personalProfileDataByIdService(id) == 0:
                    raise Exception("Personal Profile not Existed")
                else:
                    epid = personalProfileDataByIdService(id)
                    response['data'] = epid
                    response['statusCode'] = 0
        elif request.method == "PUT":

            try:

                id = int(id)
            except:
                raise Exception("Profile ID must be a Number(Integer)")
            if id <= 0:
                raise Exception("Profile ID must be a Positive number and must be Existed")
            else:
                    personalProfileEditDataByIdService(id,json.loads(request.body.decode('utf-8')))
                    response['data'] = "data has been successfully saved"
                    response['statusCode'] = 0
        else:
            response['error'] = 'Sorry unable to get the response'
            response['statusCode'] = 1
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in getting  Personal Profile data'
        response['error'] = str(e)
        response['statusCode'] = 1

    return JsonResponse(response)


@csrf_exempt
@api_view(['GET'])
def personalProfileQuestionsView(request):
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
            profileQuestions=getPersonalProfileQuestionsService()
            #print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = profileQuestions
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving Personal Profile questions'
        response['error'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@api_view(['GET'])
def getprofile(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': None
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
            all_profiles = getProfileData()

            response['data'] = 'Please enter Profile ID'
            response['error'] = 'No input Data'
            response['statusCode'] = 1
        else:
            response['error'] = 'Sorry unable to get the response'
            response['statusCode'] = 1
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Authentication error'
        response['error'] = str(e)
        response['statusCode'] = 1

    return JsonResponse(response)
