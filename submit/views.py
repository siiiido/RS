from django.shortcuts import render
from .forms import KakaoForm, UserForm
# Create your views here.

def submit(request):
    if request.method == 'GET' : 
        
        # 카카오톡 API에서 받아온 정보 KakaoForm에 입력
        
        form = KakaoForm()

        # print('kakako')
        return render(request, 'submit/submit.html', {form:form})

    elif request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid():
            # HTML에서 받아온 데이터를 UserForm에 입력
            
            return HttpResponse('Success')

        return HttpResponse('Fail')