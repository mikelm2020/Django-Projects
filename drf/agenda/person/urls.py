#
from django.urls import path, re_path

#
from . import views

app_name = "person_app"

urlpatterns = [
    path("persons/", views.PersonListView.as_view(), name="persons"),
    path(
        "api/person/list/",
        views.PersonListApiView.as_view(),
    ),
    path(
        "api/person/create/",
        views.PersonCreateApiView.as_view(),
    ),
    path("api/person/detail/<pk>/", views.PersonDetailApiView.as_view(), name="detail"),
    path(
        "api/person/delete/<pk>/",
        views.PersonDeleteApiView.as_view(),
    ),
    path(
        "api/person/update/<pk>/",
        views.PersonUpdateApiView.as_view(),
    ),
    path(
        "api/person/modify/<pk>/",
        views.PersonRetrieveUpdateApiView.as_view(),
    ),
    path(
        "api/persons/list/",
        views.PersonApiList.as_view(),
    ),
    path(
        "api/meeting/list/",
        views.MeetingListApiView.as_view(),
    ),
    path(
        "api/meetings-link/",
        views.MeetingListLinkApiView.as_view(),
    ),
    path(
        "api/person/pagination/",
        views.PersonPaginationList.as_view(),
    ),
    path(
        "api/meeting/by-job/",
        views.MeetingByPersonJob.as_view(),
    ),
]
