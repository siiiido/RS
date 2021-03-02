from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE

@csrf_protect
def main(request):
    return render(request, 'main/main.html')

    # 정검중 페이지 링크
    # context = {'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
    # return render(request, 'main/main_matching.html', context)
