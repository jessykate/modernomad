from django.urls import include, re_path, path
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.http import HttpResponse, HttpResponseRedirect
from modernomad.urls import user
import modernomad.views
import modernomad.core.urls.location
import django.views
import bank.urls
import gather.views
import api.urls
# import jwt_auth.views
# import graphapi.urls


admin.autodiscover()

urlpatterns = [
    re_path(r'^$', modernomad.views.index),
    re_path(r'^about/$', modernomad.views.about),
    re_path(r'^membership/$', modernomad.views.membership, name="membership"),
    re_path(r'^host/$', modernomad.views.host, name='host'),
    re_path(r'^stay/$', modernomad.views.stay),
    re_path(r'^404/$', modernomad.views.ErrorView),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^people/', include(modernomad.urls.user)),
    re_path(r'^locations/', include(modernomad.core.urls.location)),
    re_path(r'^events/$', gather.views.upcoming_events_all_locations),
    re_path(r'^events/emailpreferences/(?P<username>[\w\d\-\.@+_]+)/$', gather.views.email_preferences, name='gather_email_preferences'),
    re_path(r'^accounts/', include(bank.urls)),
    re_path(r'^drft/$', modernomad.views.drft),

    # various other useful things
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    re_path(r'^robots\.txt$', modernomad.views.robots),

    # api things
    # re_path(r'^api-token-auth/', jwt_auth.views.obtain_jwt_token),
    re_path(r'^api/', include(api.urls)),
    # re_path(r'^', include(graphapi.urls)),
]

# media url hackery.
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += [
    re_path(r'^%s/(?P<path>.*)$' % media_url, django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        print("Django Debug Toolbar Not Installed!")
