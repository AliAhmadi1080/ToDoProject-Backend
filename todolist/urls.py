from django.urls import path
from . import views 


urlpatterns = [
    path('listtodo/',views.list_todo),
    path('detailtodo/<int:pk>',views.detail_todo),
    path('createtodo/',views.create_todo),
    path('changetodo/<int:pk>',views.change_todo),
    path('deletetodo/<int:pk>',views.delete_todo),
]