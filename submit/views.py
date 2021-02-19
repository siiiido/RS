from django.http import HttpResponseRedirect

from django.shortcuts import render

from .models import *



# Create your views here.

def submit(request):
    if request.method == "GET":
        print("get")
        return render(request, 'submit/submit.html')
    elif request.method == "POST" :
        # test = request.POST.get('title')
        # print(test)
        # context={}


        return render(request,'submit/submit.html',context) 
        


        



        # kakao = request.POST.get('kakao')
        # uni_photo = request.POST.get('uni-photo')
        # cc_radio = request.POST.get('cc_radio')


        # question=[]

        # for i in range(1,11):
        #     question.append(request.POST.get('q'+str(i)))



        # # print("카카오 id :" + kakao,"학생증 사진 : " + uni_photo, "cc_radio : "+cc_radio)
        # print("카카오 : {}, 학생증 사진 : {}, cc확인 : {}".format(kakao,uni_photo,cc_radio))

        # print("2지 선다 답 : {}".format(question))

        
        # context = {}
        # print("post 이제 여기서 어떻게 하는가")
        # return render(request,'submit/submit.html') 
