from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud_quiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="dashboard.html")),
    url(r'^index/', TemplateView.as_view(template_name="index.html")),
    url(r'^q/', include('quiz.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'common.views.login_user'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^register/', 'common.views.register_user'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
