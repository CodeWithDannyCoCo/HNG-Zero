from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    try:
        email = "simplytobs@gmail.com"
        current_datetime = datetime.now(pytz.UTC).isoformat() + 'Z'
        github_url = "https://github.com/CodeWithDannyCoCo/HNG-Zero.git"
    
        data = {
            'email': email,
            'current_datetime': current_datetime,
            'github_url': github_url
        }
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    


