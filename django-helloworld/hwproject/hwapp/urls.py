from django.urls import path

from . import views


urlpatterns = [
    # Acces default, without any pages.
    path("", views.helloworld, name="phrases"),
    # To data by using insexes of pages "pk=localhost/<number of data ID>".
    path("<int:pk>/", views.helloworld, name="phrases"),

]
