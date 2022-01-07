from django.urls import include, re_path
from modernomad.core.views.unsorted import *

# custom management patterns
urlpatterns = [
    re_path(r'^payments/$', payments_today, name='location_payments_today'),
    re_path(r'^payments/(?P<year>\d+)/(?P<month>\d+)$', payments, name='location_payments'),
    re_path(r'^today/$', manage_today, name='manage_today'),
    re_path(r'bookings/$', BookingManageList, name='booking_manage_list'),
    re_path(r'booking/create/$', BookingManageCreate, name='booking_manage_create'),
    re_path(r'booking/(?P<booking_id>\d+)/$', BookingManage, name='booking_manage'),
    re_path(r'booking/(?P<booking_id>\d+)/action/$', BookingManageAction, name='booking_manage_action'),
    re_path(r'booking/(?P<booking_id>\d+)/paywithdrft/$', BookingManagePayWithDrft, name='booking_manage_pay_drft'),
    re_path(r'booking/(?P<booking_id>\d+)/togglecomp/$', BookingToggleComp, name='booking_toggle_comp'),
    re_path(r'booking/(?P<booking_id>\d+)/sendreceipt/$', BookingSendReceipt, name='booking_send_receipt'),
    re_path(r'booking/(?P<booking_id>\d+)/sendwelcome/$', BookingSendWelcomeEmail, name='booking_send_welcome'),
    re_path(r'booking/(?P<booking_id>\d+)/sendmail/$', BookingSendMail, name='booking_send_mail'),
    re_path(r'bill/(?P<bill_id>\d+)/charge/$', BillCharge, name='bill_charge'),
    re_path(r'bill/(?P<bill_id>\d+)/payment/$', ManagePayment, name='manage_payment'),
    re_path(r'bill/(?P<bill_id>\d+)/addbillitem/$', AddBillLineItem, name='add_bill_item'),
    re_path(r'bill/(?P<bill_id>\d+)/deletebillitem/$', DeleteBillLineItem, name='delete_bill_item'),
    re_path(r'bill/(?P<bill_id>\d+)/recalculate/$', RecalculateBill, name='recalculate_bill'),
    re_path(r'booking/(?P<booking_id>\d+)/edit/$', BookingManageEdit, name='booking_manage_edit'),
    re_path(r'^subscription/(?P<subscription_id>\d+)/bill/(?P<bill_id>\d+)/sendreceipt/$', SubscriptionSendReceipt, name='subscription_send_receipt'),
    re_path(r'^subscriptions/(?P<subscription_id>\d+)/sendmail/$', SubscriptionSendMail, name='subscription_send_mail'),
    re_path(r'^subscriptions/create$', SubscriptionManageCreate, name='subscription_manage_create'),
    re_path(r'^subscriptions/(?P<subscription_id>\d+)/$', SubscriptionManageDetail, name='subscription_manage_detail'),
    re_path(r'^subscriptions/(?P<subscription_id>\d+)/update_end_date/$', SubscriptionManageUpdateEndDate, name='subscription_manage_update_end_date'),
    re_path(r'^subscriptions/(?P<subscription_id>\d+)/generateallbills/$', SubscriptionManageGenerateAllBills, name='subscription_manage_all_bills'),
    re_path(r'^subscriptions/$', SubscriptionsManageList, name='subscriptions_manage_list'),
]
