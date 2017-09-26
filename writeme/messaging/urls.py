from django.conf.urls import include, url
from .views import MessagesView, NewMessageView

app_name = 'messaging'
urlpatterns = [
    url(r'^$', MessagesView.as_view(), name='messages'),
    url(r'^new/(?P<username>\w+)/$', NewMessageView.as_view(), name='new'),
    url(r'^new/$', NewMessageView.as_view(), name='new')
]