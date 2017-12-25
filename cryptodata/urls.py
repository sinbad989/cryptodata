from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.data_list, name='data_list'),
    url(r'^about/$',views.data_list, name='about'),
]