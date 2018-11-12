from django.urls import path
from . import views #현재폴더(todo)에 있는 views 파일 추가


app_name='todo'

urlpatterns = [
    path('', views.index), #/todos 가 이미 되있음(생략)
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/', views.read),
    path('todo_create/', views.todo_create),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),

]