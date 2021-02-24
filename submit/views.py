from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from social.models import Social_User_Table

import requests
import json


# =============상한-=============

def submit(request):
    
    session_user_id = request.session.get('user')

    if request.method == "GET":

        if session_user_id :
            user_info = Social_User_Table.objects.get(pk=session_user_id)
            context = {'user' : user_info}
<<<<<<< HEAD
            return render(request, 'submit/submit_test.html', context)
        user = request.session.get('user')

        if user:
            social_user = Social_User_Table.objects.get(pk=user)
            context = {'user': social_user}
            return render(request, 'submit/submit.html', context)

        else:
            return redirect('/')
=======
            return render(request, 'submit/submit.html', context)
        
        else :            
            return redirect('/')      
>>>>>>> 9cf4722d13aa408b6419a4ffb71fee6c32a16143

    elif request.method == "POST":
        """
        1. 페이지 내 데이터 받기
        2. 데이터 DB 반영
        3. 페이지 전환
        """
        user_info = Social_User_Table.objects.get(pk=session_user_id)

        print(user_info.gender)
        print(user_info.age_range)

        """ 
        상한 테스트 파트
        """

        # user = request.session.get('user')
        # print(user)

        html_user_nickname = request.POST.get('html_user_nickname', '')
        print("html_user_nickname : ", html_user_nickname)
        print("asdsa")

        # select, option 데이터 넘길 때
        html_university = request.POST['html_university']
        print("html_university : ", html_university)

        html_contact = request.POST.get('html_contact')
        print("html_contact : ", html_contact)

        html_image = request.POST.get('html_image')
        print("html_image : ", html_image)

        html_preference = request.POST.get('html_preference')
        print("html_preference : ", html_preference)

        html_Q01 = request.POST.get('html_Q01')
        print("html_Q01 : ", html_Q01)

        html_Q02 = request.POST.get('html_Q02')
        print("html_Q02 : ", html_Q02)

        html_Q03 = request.POST.get('html_Q03')
        print("html_Q03 : ", html_Q03)

        html_Q08 = request.POST.get('html_Q08')
        print("html_Q08 : ", html_Q08)

        # social_user = Social_User_Table.objects.get(pk=user)

        # Social_User_Table(
        #         user_id         = user,
        #         contact         = html_data,
        #     ).save()
        


        
        # html_data = request.POST.get('title')
        # print(html_data)
        
        # return render(request, "submit/submit_test.html")

        print("post fin")

        return redirect('/status')