from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length= 50) #스트링 타입을 저장하는 필드,최대길이 50으로 줌
    deadline = models.DateField()
    
    
    def __str__(self):
        return self.title #원랜 todo object 였는데 오버라이딩 해줬음