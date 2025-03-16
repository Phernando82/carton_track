from django.urls.conf import path

from carton_track_project.base.views import home

app_name = "base"
urlpatterns = [
    path("", home, name="home"),
]
