from django.urls import include, re_path

from modernomad.core.views.booking import *
from modernomad.core.views.unsorted import submit_payment

# urls starting in /booking get sent here.
urlpatterns = [
    re_path(r'^(?P<booking_uuid>[0-9a-f\-]+)/payment/$', submit_payment, name='booking_payment'),
]

urlpatterns += [
    re_path(r'^submit$', BookingSubmit, name='booking_submit'),
    re_path(r'^(?P<booking_id>\d+)/$', BookingDetail, name='booking_detail'),
    re_path(r'^(?P<booking_id>\d+)/receipt/$', BookingReceipt, name='booking_receipt'),
    re_path(r'^(?P<booking_id>\d+)/edit/$', BookingEdit, name='booking_edit'),
    re_path(r'^(?P<booking_id>\d+)/confirm/$', BookingConfirm, name='booking_confirm'),
    re_path(r'^(?P<booking_id>\d+)/delete/$', BookingDelete, name='booking_delete'),
    re_path(r'^(?P<booking_id>\d+)/cancel/$', BookingCancel, name='booking_cancel'),
]
