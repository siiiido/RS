from django.http import HttpResponse
from django.shortcuts import render

from social.models import Social_User_Table
from result.models import Matching_Table
# Create your views here.

def result(request):
    
    session_user_id = request.session.get('user')
    
    # 정보 등록 회원
    if Social_User_Table.objects.filter(user_id=session_user_id).exists() :
        user_info = Social_User_Table.objects.get(pk=session_user_id)
        
        # 남->여 매칭 성공
        if Matching_Table.objects.filter(user_man_id=user_info.user_id).exists():
            user_man_info = Matching_Table.objects.get(user_man_id=user_info.user_id)      

            user_woman_info = Social_User_Table.objects.get(user_id=user_man_info.user_woman_id)
            user_man_info = Social_User_Table.objects.get(user_id=user_man_info.user_man_id)

            # print("매칭 성공! (남->여)\n" + user_man_info.user_nickname + '님의 매칭 상대의 카카오톡 아이디는\n' + user_woman_info.contact + "입니다!")

            context = {'man' : user_man_info, 'woman' : user_woman_info}
            return render(request, 'result/result.html', context)

        # 여->남 매칭 성공
        elif Matching_Table.objects.filter(user_woman_id=user_info.user_id).exists():            
            
            user_woman_info = Matching_Table.objects.get(user_woman_id=user_info.user_id)      

            user_man_info = Social_User_Table.objects.get(user_id=user_woman_info.user_woman_id)
            user_woman_info = Social_User_Table.objects.get(user_id=user_woman_info.user_man_id)
            
            # print("매칭 성공! (남->여)\n" + user_woman_info.user_nickname + '님의 매칭 상대의 카카오톡 아이디는\n' + user_man_info.contact + "입니다!")
                        
            context = {'man' : user_man_info, 'woman' : user_woman_info}
            return render(request, 'result/result.html', context)
        
        # 매칭 실패
        else:
            return HttpResponse('매칭 실패 다음 기회에')
        
    # 정보 미등록 회원
    else:
        return HttpResponse('매칭 등록 X')