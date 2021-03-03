from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render, redirect

from datetime import date
from social.models import Social_User_Table
from main.models import Registered_User_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE, SUBMIT_DATE

@csrf_protect
def result(request):
    
    session_user_info = request.session.get('user_info')
    
    # 로그인 O
    if session_user_info :

        # RDB 등록 O / SDB 등록 X
        if Registered_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists() and not Social_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists():
            registered_user = Registered_User_Table.objects.get(user_id=session_user_info.get('user_id'))

            # RDB 매칭일 == LAST_DATE
            # RDB 매칭 성공
            if registered_user.last_partner_user_id != '' and registered_user.recent_matching_date == LAST_DATE:
                partner_info = Registered_User_Table.objects.get(last_partner_user_id=registered_user.user_id)    
                context = {'my_info' : registered_user, 'partner_info' : partner_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE, 'SUBMIT_DATE' : SUBMIT_DATE}

                return render(request, 'result/result_succes.html', context)

            # RDB 매칭 실패
            else:                
                context = {'my_info' : registered_user, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                return render(request, 'result/result_fail.html', context)
                
            
            # RDB 매칭일 != LAST_DATE
            return redirect('/submit')

        # SDB 등록 회원
        elif Social_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists() :
            user_info = Social_User_Table.objects.get(user_id=session_user_info.get('user_id'))

            # 관리자 승인 대기
            if user_info.admin_allow == None :
                
                context = {'my_info' : user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                return render(request, 'result/result_not_approve.html', context)
                                
            # 관리자 승인 O
            elif user_info.admin_allow:
                # 매칭일 이전 연결
                context = {'my_info' : user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                return render(request, 'result/result_allow_ok.html', context)
                
                """
                # 매칭일 이후 연결
                my_info = Registered_User_Table.objects.get(user_id=session_user_info.get('user_id'))
                # 매칭 실패
                if my_info.last_partner_user_id == '':
                    context = {'my_info' : user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                    return render(request, 'result/result_fail.html', context)

                # 매칭 성공
                else:
                    partner_info = Registered_User_Table.objects.get(last_partner_user_id=my_info.user_id)
       
                    context = {'my_info' : my_info, 'partner_info' : partner_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                    return render(request, 'result/result_succes.html', context)
                """
            # 관리자 승인 X
            else:                       
                context = {'my_info' : user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
                return render(request, 'result/result_deny.html', context)
           
    # 로그인 X
    else:
        return redirect('/')








