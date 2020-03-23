from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.functions.metadata import getConfig, configureLogging
from dashboard.functions.dashboard_service import saveDashboardService,dashboardService
import logging
from django.shortcuts import render, get_object_or_404
import json
from rest_framework.decorators import api_view
from dashboard.functions.database import saveDashboardDB

@csrf_exempt
@api_view(['GET', 'POST'])
def dashboardView(request):
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
            saveDashboardService(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = 'dashboard data saved successfully'

        else:
            all_profiles = dashboardService()
            response['data'] = all_profiles
            response['statusCode'] = 0
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving dashboard data'
        response['error'] = str(e)
    return JsonResponse(response)