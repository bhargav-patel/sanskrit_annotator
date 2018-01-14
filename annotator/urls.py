from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word_id>[0-9]+)/$', views.change_word, name='change_word'),
    url(r'select/(?P<wordoption_id>[0-9]+)/$', views.select_wordoption, name='select_wordoption'),
    url(r'eliminate/(?P<wordoption_id>[0-9]+)/$', views.eliminate_wordoption, name='eliminate_wordoption'),
    url(r'undo/(?P<word_id>[0-9]+)/$', views.undo_selections, name='undo_selections'),
    url(r'change_encoding$', views.change_encoding, name='change_encoding'),
    url(r'change_all$', views.change_all, name='change_all'),
    url(r'reset_session$', views.reset_session, name='reset_session'),
]