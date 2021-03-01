from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

@csrf_protect
def main(request):
    return render(request, 'main/main.html')
