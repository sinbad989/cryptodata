from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.data_list, name='data_list'),
    url(r'^about/$',views.about, name='about'),
    url(r'^home/$',views.home, name='home'),
    url(r'^search/',views.search, name='search'),
]