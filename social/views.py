from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from config.settings import SECRET_KEY

from .models import Social_User, Social_Platform

import requests
import json
import jwt


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
        # access_token = request.headers.get('Authorization', None)

        # print( token_kakao_response.text )
        # print( access_token )

        url = 'https://kapi.kakao.com/v2/user/me'
        headers = {
            'Authorization' : f'Bearer {access_token}',
            'Content-type' : 'application/x-www-form-urlencoded; charset=utf=8'
        }

        kakao_response = requests.get(url, headers = headers)
        kakao_response = json.loads(kakao_response.text)

        print("kakao_response")
        print(kakao_response)
        print("kakao_response")

        # # get        
        # # kakao = Social_Platform.objects.get(platform_name='kakao')
        
        # # filter
        # kakao = Social_Platform.objects.filter(platform_name='kakao')

        # # get_object_or_404()
        # # kakao = get_object_or_404(Social_Platform, platform_name='kakao')
            
        # print("kakao")
        # print(kakao)
        # print("kakao")

        # if Social_User.objects.filter(platform = kakao, user_id = kakao_response["id"]).exists():
            
        #     social_user = Social_User.objects.get(platform_id = kakao_response['id'])
        #     jwt_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = 'HS256').decode('urf=8')

        #     return HttpResponse(f'id:{social_user.user_id}, name:{social_user.user_name}, token:{jwt_token}')
        

        # print("카카오 아이디")
        # print(kakao_response['id'])
        # print("카카오 아이디")

        # Social_User(
        #     user_id         = kakao_response['id'],
        #     user_name       = kakao_response['properties']['nickname'],
        #     social_platform = kakao,
        #     email           = kakao_response['kakao_account'].get('email', None)
        # ).save()

        # social_user = Social_User.objects.get(social_platform = kakao, user_id = kakao_response['id'])
        # marpple_tokken = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = 'HS256').decode('urf=8')

        # return HttpResponse(f'id:{social_user.user_id}, name:{social_user.user_name}, token:{marpple_tokken}')
        


        # kakao = ' '
        # try:            
        #     kakao = Social_Platform.objects.get(platform_name='kakao')

        #     print("Test 5")

        #     if Social_User.objects.filter(platform = kakao, user_id = kakao_response['id']).exists():
                
        #         social_user = Social_User.objects.get(user_id = kakao_response['id'])
        #         jwt_token = jwt.encode({'user_id':social_user.user_id}, SECRET_KEY, algorithm = 'HS256').decode('utf=8')

        #         print(  'user_id : ' + social_user.user_id +
        #                 '\nuser_name : ' + social_user.user_name +
        #                 '\ntoken : ' + jwt_token )
                
        #         # return redirect('/submit')
        #         return HttpResponse(f'user_id:{social_user.user_id}, user_name:{social_user.user_name}, token:{jwt_token}')
    
        # except:

        #     print("test 6")

        #     Social_User(
        #         user_id         = kakao_response['id'],
        #         user_name       = kakao_response['properties']['nickname'],
        #         platform        = kakao,
        #         email           = kakao_response['kakao_account'].get('email', None)
        #     ).save()

        #     social_user = Social_User.objects.get(platform = kakao, user_id = kakao_response['id'])
        #     marpple_tokken = jwt.encode({'user_id':social_user.user_id}, SECRET_KEY, algorithm = 'HS256').decode('utf=8')

        #     print(  'user_id : ' + social_user.user_id +
        #                 '\nuser_name : ' + social_user.user_name +
        #                 '\ntoken : ' + marpple_tokken )

        #     # return redirect('/submit')
        #     return HttpResponse(f'user_id:{social_user.user_id}, user_name:{social_user.user_name}, token:{marpple_tokken}')


        print("kakakakao")
                  
        kakao = 'kakao'

        if Social_User.objects.filter(platform = kakao, user_id = kakao_response['id']).exists():
            
            social_user = Social_User.objects.get(user_id = kakao_response['id'])
            jwt_token = jwt.encode({'user_id':social_user.user_id}, SECRET_KEY, algorithm = 'HS256').decode('utf=8')

            print(  'user_id : ' + social_user.user_id +
                    '\nuser_name : ' + social_user.user_name +
                    '\ntoken : ' + jwt_token )

            return redirect('/submit')
            # return HttpResponse(f'user_id:{social_user.user_id}, user_name:{social_user.user_name}, token:{jwt_token}')

        Social_User(
            user_id         = kakao_response['id'],
            user_name       = kakao_response['properties']['nickname'],
            platform        = kakao,
            email           = kakao_response['kakao_account'].get('email', None)
        ).save()

        social_user = Social_User.objects.get(platform = kakao, user_id = kakao_response['id'])
        marpple_tokken = jwt.encode({'user_id':social_user.user_id}, SECRET_KEY, algorithm = 'HS256').decode('utf=8')

        print(  'user_id : ' + social_user.user_id +
                    '\nuser_name : ' + social_user.user_name +
                    '\ntoken : ' + marpple_tokken )
        return redirect('/submit')
        # return HttpResponse(f'user_id:{social_user.user_id}, user_name:{social_user.user_name}, token:{marpple_tokken}')
        
        
