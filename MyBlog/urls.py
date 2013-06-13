from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # ArticleApp
    url(r'^$','ArticleApp.views.index',name='index'),
    url(r'^board/(\w+)/(\d*)$','ArticleApp.views.board',name='board'),
    url(r'^board/(\w+)/$','ArticleApp.views.board',name='board'),
    url(r'^article/(\d+)/$','ArticleApp.views.article',name='article'),
    url(r'^404/$','ArticleApp.views._404',name='404'),


    # AccountApp
    url(r'^login/$', 'AccountApp.views.login', name='login'),
    url(r'^logout/$', 'AccountApp.views.logout', name='logout'),
    url(r'^profile/$', 'AccountApp.views.profile', name='profile'),
)
