from django.urls import path
from . import views 


urlpatterns = [
    path('',views.ToDoMixinList.as_view()),
    path('<int:pk>/',views.ToDoMixinDetail.as_view()),
]