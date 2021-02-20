from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from social.models import Social_User_Table

import requests
import json

def submit(request):

    if request.method == "GET":

        user = request.session.get('user')
        
        if user :
            social_user = Social_User_Table.objects.get(pk=user)
            context = {'user' : social_user}
            return render(request, 'submit/submit_test.html', context)
        
        else :            
            return redirect('/')      

    elif request.method == "POST":
        """
        1. 페이지 내 데이터 받기
        2. 데이터 DB 반영
        3. 페이지 전환
        """
        html_data = request.POST.get('title')
        print(html_data)

        

        user = request.session.get('user')
        print(user)
        social_user = Social_User_Table.objects.get(pk=user)

        Social_User_Table(
                user_id         = user,
                contact         = html_data,
            ).save()
        

        
        print("post fin")

        return render(request, "submit/submit_test.html")