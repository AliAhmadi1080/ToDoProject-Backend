from django.urls import path
from . import views 


urlpatterns = [
    path('',views.ToDoList.as_view()),
    path('usertodo',views.UserToDo.as_view()),
    path('<int:pk>/',views.ToDoGenericsDetail.as_view()),
]