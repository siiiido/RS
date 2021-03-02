from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from social.models import Social_User_Table
from main.models import Registered_User_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE


@csrf_protect
def status(request):

    session_user_info = request.session.get('user_info')

    if Registered_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists():
        recent_matching_user = Registered_User_Table.objects.get(user_id=session_user_info.get('user_id'))
        # 모든 DB에 매칭 날짜가 최근 날짜
        if recent_matching_user.last_update_date == LIST_DATE[0]:
            # 여기에 submit fail 페이지 링크            
            context = {'user' : recent_matching_user, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
            return render(request, 'status/status.html', context)    


    if session_user_info :
        
        # print("정보 등록 완료!\n" + user_info.user_nickname + "님 정상등록 되었습니다.")
        # print("관리자 승인을 기다려주세요!")
        # print("다음 매칭일은 N월 N일입니다.")

        context = {'user' : session_user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}      
        return render(request, 'status/status.html', context)

    else:
        return redirect('/')

    
