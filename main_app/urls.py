from django.conf.urls import url
from main_app import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^([0-9]+)/$', views.detail, name="detail"),
    url(r'^new/$', views.post_listing, name="post_listing"),
    url(r'^user/(\w+)/$', views.profile, name="profile"),
    url(r'^request_form/$', views.request_form, name="request_form"),
    url(r'^delete/(?P<pk>\d+)$', views.delete_listing, name='delete_listing'),
    url(r'^edit/(?P<pk>\d+)$', views.update_listing, name='update_listing'),
]
