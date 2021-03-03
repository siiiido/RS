from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from social.models import Social_User_Table
from main.models import Registered_User_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE


@csrf_protect
def status(request):

    session_user_info = request.session.get('user_info')

    if Registered_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists() :
        recent_matching_user = Registered_User_Table.objects.get(user_id=session_user_info.get('user_id'))
        # 모든 DB에 매칭 날짜가 최근 날짜
        if recent_matching_user.recent_matching_date == LAST_DATE:
            # 여기에 submit fail 페이지 링크            
            context = {'user' : recent_matching_user, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
            return render(request, 'status/status_matching_success.html', context)    
        else:
            return redirect('/submit')

    elif Social_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists() :
        context = {'user' : session_user_info, 'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}      
        return render(request, 'status/status.html', context)

    else:
        return redirect('/')

    
