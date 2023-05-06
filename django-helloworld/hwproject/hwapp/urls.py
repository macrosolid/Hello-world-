from django.urls import path

from . import views


urlpatterns = [

    # path("<int:pk>/", views.helloworld, name="phrases"),
    path("", views.helloworld, name="phrases"),
    path("<int:pk>/", views.helloworld, name="phrases"),

]
