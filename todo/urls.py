from django.urls import path
from . import views #현재폴더(todo)에 있는 views 파일 추가

urlpatterns = [
    path('', views.index), #/todos 가 이미 되있음
    path('new/', views.new),

]