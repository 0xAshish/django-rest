from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from backend import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/$',views.register.as_view(),  ),
    url(r'^api/login/$', auth_views.login, name='login'),
    url(r'^api/logout/$', auth_views.logout,  name='logout'),
    url('^register/', views.register.as_view(), name='register'),
]
