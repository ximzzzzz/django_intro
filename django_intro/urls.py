"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include 해야함 ㅎ
from django_app import views   #설정한 django_app 폴더 안에 있는 view.py를 가져오기!


# app.route 설정과 비슷한 원리
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),  #path('url', 메소드)     #플라스크처럼 아래에 함수를 정의하는게 아닌, view.py에 정의한다
    path('whoami/', views.me),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    path('hello/<str:name>/', views.hello), #헬로 뒤에 뭐가들어와도 name변수에 담기게됨
    path('cube/<int:cube_num>/', views.cube),
    #인자 컨버터
    # str:스트링
    #int : 0또는 양의정수
    #slug : 문자 또는 숫자, 하이픈, 밑줄
    path('todos/', include('todo.urls')) #todo라는 앱 안에 urls 내용을 포함시키겠다
    
]
