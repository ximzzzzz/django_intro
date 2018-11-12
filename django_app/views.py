from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
    
def me(request):
    return render(request, 'me.html')
    
def lunch(request):
    menu_list = ['김카', '20층']
    pick = random.choice(menu_list)
    return render(request, 'lunch.html', {'pick':pick})
    
def lotto(request):
    lotto_number = random.sample(range(1,46),6)
    return render(request, 'lotto.html', {'lotto_number':lotto_number})
    
def hello(request,name): #name 인자값 받았음
    return render(request, 'hello.html', {'name':name})

def cube(request, cube_num):
    result = cube_num**3
    return render(request, 'cube.html', {'result':result})