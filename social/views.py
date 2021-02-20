"""
선택동의항목 뜨지 않을 경우 아래 사이트에서 프로필 지정 해야함
https://accounts.kakao.com/

로그인시 session 생성함

로그아웃 구현시 session.pop 해야함!
https://infinitt.tistory.com/221
"""


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from config.settings import SECRET_KEY

from django.db import models
from .models import Social_User_Table

import requests
import json


# Create your views here.
class kakaoLoginView(View):
    def get(self, request):
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

        # 수정 예정
        # 왜 전역으로 선언해야하는지를 모르겟음
        global Social_User_Table        
        if Social_User_Table.objects.filter(user_nickname = kakao_response['properties']['nickname'], user_id = kakao_response['id']).exists():
            
            Social_User_Table = Social_User_Table.objects.get(user_id = kakao_response['id'])
            
            request.session['user'] = Social_User_Table.user_id

        else :
            Social_User_Table(
                user_id         = kakao_response['id'],
                user_nickname   = kakao_response['properties']['nickname'],
                gender          = kakao_response['kakao_account']['gender'],
                age_range       = kakao_response['kakao_account']['age_range'],
            ).save()

            Social_User_Table = Social_User_Table.objects.get(user_id = kakao_response['id'])
           
            request.session['user'] = Social_User_Table.user_id
        
        return redirect('/submit')  