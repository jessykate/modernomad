from django.urls import include, re_path
import modernomad.core.views.unsorted
from modernomad.core.views import location
import modernomad.core.emails.messages
import modernomad.core.urls.bookings
import modernomad.core.urls.uses
import modernomad.core.urls.manage
import modernomad.core.views.redirects
import gather.urls

per_location_patterns = [
    re_path(r'^$', location.LocationDetail.as_view(), name='location_detail'),
    re_path(r'^stay/$', modernomad.core.views.booking.StayView.as_view(), name='location_stay'),
    re_path(r'^stay/room/(?P<room_id>\w+)$', modernomad.core.views.booking.StayView.as_view(), name='room'),
    re_path(r'^community/$', modernomad.core.views.unsorted.community, name='location_community'),
    re_path(r'^team/$', modernomad.core.views.unsorted.team, name='location_team'),
    re_path(r'^guests/$', modernomad.core.views.unsorted.guests, name='location_guests'),
    re_path(r'^occupancy/$', modernomad.core.views.unsorted.occupancy, name='location_occupancy'),
    re_path(r'^occupancy/room/(?P<room_id>\d+)/(?P<year>\d+)/$', modernomad.core.views.unsorted.room_occupancy, name='room_occupancy'),
    re_path(r'^calendar/$', modernomad.core.views.unsorted.calendar, name='location_calendar'),
    re_path(r'^thanks/$', modernomad.core.views.unsorted.thanks, name='location_thanks'),
    re_path(r'^today/$', modernomad.core.views.unsorted.today, name='location_today'),

    re_path(r'^json/room/$', modernomad.core.views.booking.RoomApiList.as_view(), name='json_room_list'),
    re_path(r'^json/room/(?P<room_id>\w+)/$', modernomad.core.views.booking.RoomApiDetail.as_view(), name='json_room_detail'),

    re_path(r'^edit/settings/$', modernomad.core.views.unsorted.LocationEditSettings, name='location_edit_settings'),
    re_path(r'^edit/users/$', modernomad.core.views.unsorted.LocationEditUsers, name='location_edit_users'),
    re_path(r'^edit/content/$', modernomad.core.views.unsorted.LocationEditContent, name='location_edit_content'),
    re_path(r'^edit/emails/$', modernomad.core.views.unsorted.LocationEditEmails, name='location_edit_emails'),
    re_path(r'^edit/pages/$', modernomad.core.views.unsorted.LocationEditPages, name='location_edit_pages'),
    re_path(r'^edit/rooms/(?P<room_id>\d+)/$', modernomad.core.views.unsorted.LocationEditRoom, name='location_edit_room'),
    re_path(r'^edit/rooms/new$', modernomad.core.views.unsorted.LocationNewRoom, name='location_new_room'),
    re_path(r'^edit/rooms/$', modernomad.core.views.unsorted.LocationManageRooms, name='location_manage_rooms'),

    re_path(r'^email/current$', modernomad.core.emails.messages.current, name='location_email_current'),
    re_path(r'^email/stay$', modernomad.core.emails.messages.stay, name='location_email_stay'),
    re_path(r'^email/residents$', modernomad.core.emails.messages.residents, name='location_email_residents'),
    re_path(r'^email/test80085$', modernomad.core.emails.messages.test80085, name='location_email_test'),
    re_path(r'^email/unsubscribe$', modernomad.core.emails.messages.unsubscribe, name='location_email_unsubscribe'),
    re_path(r'^email/announce$', modernomad.core.emails.messages.announce, name='location_email_announce'),

    # internal views
    re_path(r'^rooms_availabile_on_dates/$', modernomad.core.views.unsorted.RoomsAvailableOnDates, name='rooms_available_on_dates'),

    re_path(r'^booking/', include(modernomad.core.urls.bookings)),
    re_path(r'^use/', include(modernomad.core.urls.uses)),
    re_path(r'^manage/', include(modernomad.core.urls.manage)),

    re_path(r'^events/', include(gather.urls)),

    # redirect from old 'reservation' paths
    re_path(r'^reservation/(?P<rest_of_path>(.+))/$', modernomad.core.views.redirects.reservation_redirect),

]

urlpatterns = [
    re_path(r'^$', modernomad.core.views.unsorted.location_list, name='location_list'),
    re_path(r'^(?P<location_slug>[\w-]+)/', include(per_location_patterns)),
]
