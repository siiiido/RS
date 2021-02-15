from django.shortcuts import render
from social.models import Social_User

# Create your views here.

def submit(request):


    social_user = Social_User.objects.all()
    context = {'users' : social_user}
    print(social_user)

    return render(request, 'submit/submit_test.html', context)

    if requset.method == "GET":
        """
        1. kakao 데이터를 포함하기
        2. html 불러오기
        """
        print("get")
        
    elif request.method == "POST":
        """
        1. 페이지 내 데이터 받기
        2. 데이터 DB 반영
        3. 페이지 전환
        """
        print("post")

    # elif request.method == "POST" :
    #     return 