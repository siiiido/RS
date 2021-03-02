from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from config.settings import LIST_DATE

@csrf_protect
def main(request):
    return render(request, 'main/main.html')

    # 정검중 페이지 링크
    # context = {'LIST_DATE' : LIST_DATE}
    # return render(request, 'main/main.html', context)
