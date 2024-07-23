from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Tag(models.Model):
    name = models.CharField('نام تگ',max_length=63)
    created = models.DateField("زمان ایجاد شدن",auto_created=True,auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'تگ'    
        verbose_name_plural = 'تگ ها'    

class Status(models.Model):
    name = models.CharField(max_length=63,verbose_name="نام")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'


class ToDo(models.Model):
    title         = models.CharField('عنوان',max_length=63)
    subtitle     = models.CharField('زیر عنوان',max_length=63)
    user         = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر',related_name='todos')
    status       = models.ForeignKey("Status",on_delete=models.SET_DEFAULT,default='انجام نشده',verbose_name="وضعیت")
    description  = models.TextField('توضیحات',null=True)
    created_at   = models.DateTimeField(auto_now_add=True,verbose_name='زمان شروع',editable=False)
    tags         = models.ManyToManyField('Tag',verbose_name='تگ ها')


    # TODO:add subtasks to class

    def __str__(self) -> str:
        return f"{self.name} -> {self.status}"

    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظیفه ها'



class ToDoList(models.Model):
    name = models.CharField('نام',max_length=63)
    todos = models.ManyToManyField(ToDo,verbose_name='وظیفه ها')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'لیست وظیفه'
        verbose_name_plural = 'لیست وظیفه ها'