from django.urls import path
from . import views 


urlpatterns = [
    path('',views.ToDoCreate.as_view()),
    path('usertodo',views.UserToDoList.as_view()),
    path('todolist',views.ToDoListAPI.as_view()),
    path('tag',views.UserTag.as_view()),
    path('tagtodo/<slug:slug>/',views.TagToDo.as_view()),
    path('status',views.UserStatus.as_view()),
    path('<int:pk>/',views.ToDoGenericsDetail.as_view()),
]