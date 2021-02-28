from django.http import HttpResponse
from django.shortcuts import render, redirect

from social.models import Social_User_Table

def result(request):
    
    session_user_id = request.session.get('user')
    
    # 로그인 O
    if session_user_id :
        # 정보 등록 회원
        if Social_User_Table.objects.filter(user_id=session_user_id).exists() :
            user_info = Social_User_Table.objects.get(pk=session_user_id)

            # 관리자 승인 대기
            if user_info.admin_allow == None :
                
                print("관리자 승인 대기중!\n" + user_info.user_nickname + '님!')
                
                context = {'my_info' : user_info}
                return render(request, 'result/1.html', context)
                                
            # 관리자 승인 O
            elif user_info.admin_allow:
                
                """
                # 매칭일 이전 연결
                return HttpResponse('관리자 승인 완료\n 매칭일을 기다려주세요')
                """

                # 매칭일 이후 연결
                # 매칭 성공 - 남여 구분 X
                if Social_User_Table.objects.filter(user_id=user_info.user_id).exists():                    
                    my_info = Social_User_Table.objects.get(user_id=user_info.user_id)
                    partner_info = Social_User_Table.objects.get(partner_user_id=user_info.user_id)

                    # print("매칭 성공!\n" + my_info.user_nickname + '님의 매칭 상대의 카카오톡 아이디는\n' + partner_info.contact + "입니다!")
                    
                    context = {'my_info' : my_info, 'partner_info' : partner_info}
                    return render(request, 'result/result.html', context)

                #매칭 실패
                else:
                    
                    print("매칭 실패 다음 기회에\n" + user_info.user_nickname + '님!')

                    context = {'my_info' : user_info}
                    return render(request, 'result/2.html', context)

            # 관리자 승인 X
            else:                
                
                print("관리자 승인 거절\n" + user_info.user_nickname + '님!')
                
                context = {'my_info' : user_info}
                return render(request, 'result/3.html', context)
                        
        # 정보 미등록 회원
        else:            

            print("이번 매칭에 등록되어 있지 않습니다!\n" + user_info.user_nickname + '님!')

            context = {'my_info' : user_info}
            return render(request, 'result/4.html', context)

    # 로그인 X
    else:
        return redirect('/')