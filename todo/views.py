from django.shortcuts import render, redirect
from todo.models import Todo


# Create your views here.
def index(request):
    todos= Todo.objects.all() #todo object 전부 부르기
    return render(request,'todo/index.html',{'todos':todos})
    
def new(request):
    return render(request, 'todo/new.html')
    
def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, deadline=deadline)
    todo.save() #add와 commit이 합쳐진 로직
    
    return redirect('/todos/')
    
def read(request,id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/read.html',{'todo':todo})
    
def todo_create(request):
    if request.method =='POST':
        title = request.Post.get('title')
        deadline = request.Post.get('deadline')
        Todo.objects.create(title = title, deadline=deadline) #만들고 save까지 한번에!!
        return redirect('/todos/')
        
    else:
        return render(request, 'todo/todo_create.html')
        
def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/')
    
def update(request,id):
    todo = Todo.objects.get(id=id)
    if request.method =='POST':
        todo.title = request.Post.get('title')
        todo.deadline = request.POST.get('deadline')
        todo.save()
        return redirect('/todos')
        #저장로직
        
    else:
        deadline = todo.deadline.strftime("%Y-%m-%d")
        return render(request, 'todo/update.html',{'todo':todo, 'deadline':deadline})
        #폼 보여주기 