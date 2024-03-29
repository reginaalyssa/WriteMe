from django.conf.urls import url
from .views import ConversationMessagesListView, NewMessageDisabledUserView, NewMessageView, RecentMessagesListView

app_name = 'messaging'
urlpatterns = [
    url(r'^new/(?P<username>\w+)/$', NewMessageDisabledUserView.as_view(), name='new'),
    url(r'^new/$', NewMessageView.as_view(), name='new'),
    url(r'^(?P<username>\w+)/$', ConversationMessagesListView.as_view(), name='conversation'),
    url(r'^$', RecentMessagesListView.as_view(), name='messages'),
]