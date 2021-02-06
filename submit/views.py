from django.http import HttpResponseRedirect

from django.shortcuts import render
from .forms import KakaoForm, UserForm


#-----------------------
# from .models import test
# from .forms import ContactForm
#-----------------------


def submit(request):
    # print(request.GET)
    # print(request.POST)
    # context={}
    # test_title=request.POST.get('title')
    # print(test_title)

    # print("제발 돼라 제발")
    # return render(request, "submit/submit.html", context)
    if request.method == "POST":
        print("포스트말론")
        test_title = request.POST.get('title')
        print(test_title)
    context={}
    return render(request, "submit/submit.html",context)

    # elif request.method == "GET":
    #     print("겟따뚜이")
    #     test_title = request.GET.get('title')
    #     print(test_title)
    # context={}
    # return render(request, "submit/submit.html",context)


# Create your views here.

# def submit(request):
#     if request.method == 'GET' : 
#         print(request.GET['title']) 
#         print(request.POST) 
#         print("여기는 get")
#         context={}
        

#         # 카카오톡 API에서 받아온 정보 KakaoForm에 입력
        
#         form = KakaoForm()

#         # print('kakako')
#         # templates/ : path안됬을때 해보기
#         # return render(request, 'submit/submit.html', {form:form})
#         return render(request, 'submit/submit.html',context)


#     elif request.method == 'POST' :
#         print(request.GET) 
#         print(request.POST) 
#         print("여기는 post")
#         context={}


#         # return render(request, "submit/templates/submit/submit.html", context)
#         return render(request, "submit/submit.html", context) 
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

# def mypage(request):
#     cur_user = request.user

#     if cur_user.is_authenticated:
#         user = User.objects.get(user = request.user)
#         return render(request, "main.html",{'user':user})
#     else:
#         return redirect('status')





