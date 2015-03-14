from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    #url(r'^', include('snippets.urls')),
)
