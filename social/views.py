from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from django.db import models
from datetime import date
from .models import Social_User_Table
from main.models import Registered_User_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE, SUBMIT_DATE

import requests
import json

@csrf_protect
def social(request):
    kakao_access_code = request.GET.get('code', None)
    url = 'https://kauth.kakao.com/oauth/token'
    headers = {'Content-tpye' : 'application/x-www-form-urlencoded; charset=utf-8'}

    body = {'grant_type' : 'authorization_code',
            'client_id' : '5d7075d20b4eeae726c8c1b313767b1a',
            'redirect_url' : 'http://127.0.0.1:8000/social',
            'code' : kakao_access_code}

    token_kakao_response = requests.post(url, headers = headers, data = body)
    access_token = json.loads(token_kakao_response.text).get('access_token')
    
    url = 'https://kapi.kakao.com/v2/user/me'
    headers = {
        'Authorization' : f'Bearer {access_token}',
        'Content-type' : 'application/x-www-form-urlencoded; charset=utf=8'
    }

    kakao_response = requests.get(url, headers = headers)
    kakao_response = json.loads(kakao_response.text)        

    # RDB 등록 유저
    if Registered_User_Table.objects.filter(user_id=kakao_response['id']).exists():
        user_info = {
            'user_id'       : kakao_response['id'],
            'user_nickname' : kakao_response['properties']['nickname'],
            'gender'        : kakao_response['kakao_account']['gender'],
            'age_range'     : kakao_response['kakao_account']['age_range'],
        }

        request.session['user_info'] = user_info

        date_diff = (date.today()- LAST_DATE).days
        # 매칭일 5일 이후
        if date_diff > 5:
            if Social_User_Table.objects.filter(user_id=kakao_response['id']).exists():
                return redirect('/result')

            return redirect('/submit')               
        else:
            return redirect('/result')

    # 추가 정보 동의에 대한 처리
    elif kakao_response['kakao_account']['age_range_needs_agreement'] == False and kakao_response['kakao_account']['gender_needs_agreement'] == False :

        # 이미 가입된 유저
        if Social_User_Table.objects.filter(user_id = kakao_response['id']).exists():           
            user_info = {
                'user_id'       : kakao_response['id'],
                'user_nickname' : kakao_response['properties']['nickname'],
                'gender'        : kakao_response['kakao_account']['gender'],
                'age_range'     : kakao_response['kakao_account']['age_range'],
            }

            request.session['user_info'] = user_info
            return redirect('/result')
            
        # 신규 가입 유저
        else :
            # 나이 20~29세만 가입 가능
            if kakao_response['kakao_account']['age_range'] == '20~29':     

                user_info = {
                    'user_id'       : kakao_response['id'],
                    'user_nickname' : kakao_response['properties']['nickname'],
                    'gender'        : kakao_response['kakao_account']['gender'],
                    'age_range'     : kakao_response['kakao_account']['age_range'],
                }

                request.session['user_info'] = user_info
                return redirect('/submit')  
            
            # 나이 핸들링
            else:
                # 서비스 이용 불가 안내 메시지
                context = {'user_nickname' : kakao_response['properties']['nickname']}
                return render(request, 'social/social_age.html', context)
                
    # 추가 정보 동의 핸들링
    else:
        context = {'user_nickname' : kakao_response['properties']['nickname']}
        return render(request, 'social/plus_info.html', context)