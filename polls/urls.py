
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
<<<<<<< HEAD

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('', views.IndexView, name='index123'),        
]
=======
>>>>>>> parent of ee1b3c8 (누군가 실수로 삭제 어떻게 백업할까?)
