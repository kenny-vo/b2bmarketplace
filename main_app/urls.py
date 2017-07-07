from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^([0-9]+)/$', views.show, name="show"),
    url(r'^post_url/$', views.post_listing, name="post_listing"),
    url(r'^user/(\w+)/$', views.profile, name='profile'),

]
