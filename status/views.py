from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from social.models import Social_User_Table

@csrf_protect
def status(request):

    session_user_info = request.session.get('user_info')

    if session_user_info :        

        # print("정보 등록 완료!\n" + user_info.user_nickname + "님 정상등록 되었습니다.")
        # print("관리자 승인을 기다려주세요!")
        # print("다음 매칭일은 N월 N일입니다.")

        context = {'user' : session_user_info}        
        return render(request, 'status/status.html', context)

    else:
        return redirect('/')

    
