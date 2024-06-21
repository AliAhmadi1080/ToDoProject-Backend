from django.urls import path
from . import views 


urlpatterns = [
    path('',views.ToDoGenericsList.as_view()),
    path('<int:pk>/',views.ToDoGenericsDetail.as_view()),
]