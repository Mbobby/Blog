from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chidinma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'chidinma.views.login' ),
    url(r'^logout/' , 'chidinma.views.logout'),
    url(r'^auth/', 'chidinma.views.auth_view'),
    url(r'^loggedin/', 'chidinma.views.loggedin'),
    url(r'^invalid/', 'chidinma.views.invalid'),
    url(r'^register/', 'chidinma.views.register'),
    url(r'^register_success/', 'chidinma.views.register_success')
)

#serving static files during development time
"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
"""