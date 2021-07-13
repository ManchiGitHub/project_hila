from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('talk/<str:key>/', views.chat_view, name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('listen_to_chat', views.listen_to_chat, name='listen_to_chat')
]