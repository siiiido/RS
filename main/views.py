from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE

@csrf_protect
def main(request):
    
    # 평상시
    return render(request, 'main/main.html')

    """
    # 매칭 중
    context = {'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
    return render(request, 'main/main_matching.html', context)
    """