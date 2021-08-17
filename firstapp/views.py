#firstapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #5장 추가 코드
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text']) #request의 method가 post이면, http 응답을 post방식으로 item_text를 보내라라는 뜻!!

    return render(request, 'home.html')
    #return HttpResponse('<html><title>To-Do lists</title></html>')

