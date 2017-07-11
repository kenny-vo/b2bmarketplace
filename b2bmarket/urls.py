from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('main_app.urls')),
    url(r"^messages/", include("postman.urls", namespace="postman")),

]
