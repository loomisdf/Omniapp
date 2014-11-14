from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'home.views.index'),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^signup/', include('user.urls', namespace="signup")),
    url(r'^application/', include('application.urls', namespace="application")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^about_us/', include('about_us.urls',namespace="about_us")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
