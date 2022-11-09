from django.urls import path
from .views import tasklist, taskcreate, taskdetail, taskupdate, taskdelete


# ========== app-url-patterns ==========

urlpatterns = [
    path('', tasklist, name=' tasklist'),
    path('taskcreate', taskcreate, name=' taskcreate'),
    path('taskdetail/<int:id>', taskdetail, name=' taskdetail'),
    path('taskupdate/<int:id>', taskupdate, name=' taskupdate'),
    path('taskdelete/<int:id>', taskdelete, name=' taskdelete'),
]
