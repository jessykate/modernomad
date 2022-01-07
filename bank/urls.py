from django.urls import include, re_path
from bank.views import *
from bank.views import AccountDetail, AccountList

urlpatterns = [
    re_path(r'^(?P<account_id>\d+)/$', AccountDetail.as_view(), name='account_detail'),
    re_path(r'^list/$', AccountList.as_view(), name='account_list'),
]


