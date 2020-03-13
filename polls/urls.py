from django.urls import path
from . import views

app_name = 'polls'
urlpatterns =[
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/detaill',views.detaill,name='detaill'),
    path('<int:question_id>/results',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
    path('index/',views.index, name='index'),
]