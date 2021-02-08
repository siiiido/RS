from django.http import HttpResponseRedirect

from django.shortcuts import render

# Create your views here.

def submit(request):
    if request.method == "GET":
        return render(request, 'submit/submit.html')
    # elif request.method == "POST" :
    #     return 
