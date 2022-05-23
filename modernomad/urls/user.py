from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from modernomad.core.views.unsorted import ListUsers, user_login, email_available, username_available, register, PeopleDaterangeQuery, UserDetail, UserAvatar, UserEdit, UserAddCard, UserDeleteCard, user_email_settings, user_subscriptions, user_events, user_edit_room
from modernomad.core.views.booking import UserBookings
from modernomad.core.views.redirects import old_user_bookings_redirect
from django.contrib.auth.views import *
import gather.views

import modernomad.core.forms

# Add the user registration and account management patters from the
# django-registration package, overriding the initial registration
# view to collect our additional user profile information.
# urlpatterns = patterns('',
#    re_path(r'^register/$', Registration.as_view(form_class = core.forms.UserProfileForm), name='registration_register'),
# )

urlpatterns = [
    re_path(r'^$', ListUsers, name='user_list'),
    re_path(r'^login/$', user_login, name='user_login'),
    re_path(r'^check/email$', email_available, name='email_available'),
    re_path(r'^check/username$', username_available, name='username_available'),
    re_path(r'^register/$', register, name='registration_register'),
    re_path(r'^daterange/$', PeopleDaterangeQuery, name='people_daterange'),
    re_path(r'^(?P<username>(?!logout)(?!login)(?!register)(?!check)[\w\d\-\.@+_]+)/$', UserDetail, name='user_detail'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/avatar/$', UserAvatar, name='user_avatar'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/edit/$', UserEdit, name='user_edit'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/addcard/$', UserAddCard, name='user_add_card'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/deletecard/$', UserDeleteCard, name='user_delete_card'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/email/$', user_email_settings, name='user_email_settings'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/subscriptions/$', user_subscriptions, name='user_subscriptions'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/events/$', user_events, name='user_events'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/room/(?P<room_id>\d+)/$', user_edit_room, name='user_edit_room'),
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/bookings/$', UserBookings, name='user_bookings'),
    # gracefully handle old urls
    re_path(r'^(?P<username>[\w\d\-\.@+_]+)/reservations/$', old_user_bookings_redirect),
    re_path(r'^logout/$', logout_then_login),
    re_path(r'^password/reset/$', PasswordResetView.as_view(), name="password_reset"),
    re_path(r'^password/done/$', PasswordResetDoneView.as_view(), name="password_reset_done"),
    re_path(r'^password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    re_path(r'^password/complete/$', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

# XXX can this be extracted and put into the gather app?
# TODO name collision with user_events above.
urlpatterns += re_path(r'^(?P<username>[\w\d\-\.@+_]+)/events/$', gather.views.user_events, name='user_events'),
