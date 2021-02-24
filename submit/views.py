from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from social.models import Social_User_Table

import requests
import json

def submit(request):
    
    session_user_id = request.session.get('user')

    if request.method == "GET":

        if session_user_id :
            user_info = Social_User_Table.objects.get(pk=session_user_id)
            context = {'user' : user_info}
            return render(request, 'submit/submit.html', context)
        
        else :            
            return redirect('/')      

    elif request.method == "POST":
        """
        1. 페이지 내 데이터 받기
        2. 데이터 DB 반영
        3. 페이지 전환
        """
        user_info = Social_User_Table.objects.get(pk=session_user_id)

        print(user_info.user_id)
        print(user_info.user_nickname)
        print(user_info.gender)
        print(user_info.age_range)

        """ 
        상한 테스트 파트
        """



        
        # html_data = request.POST.get('title')
        # print(html_data)
        
        return redirect('/status')
        # return render(request, "submit/submit_test.html")
