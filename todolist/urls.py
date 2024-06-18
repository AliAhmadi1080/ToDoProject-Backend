from django.urls import path
from . import views 


urlpatterns = [
    path('todolist/',views.list_todo),
    path('detailtodo/',views.detail_todo),
]