
from django.urls import path
from .views import listartasks,deletetask, updatetask

urlpatterns = [
    path('', listartasks, name="tasks"),
    path('deletetask/<int:id>',deletetask,name='deletetask'),
    path('updatetask/<int:id>',updatetask,name='updatetask'),
]
