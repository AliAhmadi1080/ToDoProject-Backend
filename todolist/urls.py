from django.urls import path
from . import views 


urlpatterns = [
    path('',views.ToDoCreate.as_view()),
    path('usertodo',views.UserToDoList.as_view()),
    path('createtodolist',views.ToDoListCreate.as_view()),
    path('<int:pk>/',views.ToDoGenericsDetail.as_view()),
]