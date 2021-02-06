from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# @is_authenticated
@csrf_exempt
def main(request):
    return render(request, 'main/main.html')
