from django.http import HttpResponseRedirect

from django.shortcuts import render
from .forms import KakaoForm, UserForm
# Create your views here.

def submit(request):
    if request.method == 'GET' : 
        
        # 카카오톡 API에서 받아온 정보 KakaoForm에 입력
        
        form = KakaoForm()

        # print('kakako')
        # templates/ : path안됬을때 해보기
        return render(request, 'submit/submit.html', {form:form})

    elif request.method == 'POST' :
        print(request.GET) 
        print(request.POST) 


        context={} 
        # return render(request, "submit/templates/submit/submit.html", context)
        return render(request, "submit/submit.html", context) 
        # # print(request.POST['your_name'])
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     # HTML에서 받아온 데이터를 UserForm에 입력
            
        #     return HttpResponse('Success')


        # return HttpResponse('Fail')


    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('')
    # else:
    #     form = UserForm()

    # return render(request, )

def mypage(request):
    cur_user = request.user

    if cur_user.is_authenticated:
        user = User.objects.get(user = request.user)
        return render(request, "main.html",{'user':user})
    else:
        return redirect('status')





