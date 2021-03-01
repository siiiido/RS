"""
선택동의항목 뜨지 않을 경우 아래 사이트에서 프로필 지정 해야함
https://accounts.kakao.com/

로그인시 session 생성함

로그아웃 구현시 session.pop 해야함!
https://infinitt.tistory.com/221
"""
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from config.settings import SECRET_KEY

from django.db import models
from .models import Social_User_Table

import requests
import json

@csrf_protect
def social(request):
    kakao_access_code = request.GET.get('code', None)
    url = 'https://kauth.kakao.com/oauth/token'
    headers = {'Content-tpye' : 'application/x-www-form-urlencoded; charset=utf-8'}

    body = {'grant_type' : 'authorization_code',
            'client_id' : '5d7075d20b4eeae726c8c1b313767b1a',
            'redirect_url' : 'http://127.0.0.1:8000/submit',
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
    
    # 추가 정보 동의에 대한 처리
    if kakao_response['kakao_account']['age_range_needs_agreement'] == False and kakao_response['kakao_account']['gender_needs_agreement'] == False :

        global Social_User_Table        
        # 이미 가입된 유저
        if Social_User_Table.objects.filter(user_nickname = kakao_response['properties']['nickname'], user_id = kakao_response['id']).exists():
            
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
                return HttpResponse('한국나이 기준 20대 만 이용 가능합니다.')
    # 추가 정보 동의 핸들링
    else:
        # 카카오톡 - 설정 - 개인/보안 - 카카오계정 - 계정 연결
        # - 연결된 서비스 관리 - 외부 서비스 - 새봄 - 모든정보 삭제 - 연결 끊기
        return HttpResponse('추가 정보 동의해주세요')