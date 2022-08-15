from django.shortcuts import render

from .models import Person, Meeting
from django.views.generic import ListView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from .serializers import (
    MeetingSerializerLink,
    PersonSerializer,
    PersonaSerializer,
    MeetingSerializer,
    PersonSerializer2,
    MeetingSerializerLink,
    PersonPagination,
    CountMeetingSerializer,
)


class PersonListView(ListView):
    context_object_name = "persons"
    template_name = "person/persons.html"

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonDetailApiView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteApiView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateApiView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonApiList(ListAPIView):
    """
    View for interact with serializers
    """

    serializer_class = PersonSerializer2

    def get_queryset(self):
        return Person.objects.all()


class MeetingListApiView(ListAPIView):

    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()


class MeetingListLinkApiView(ListAPIView):

    serializer_class = MeetingSerializerLink

    def get_queryset(self):
        return Meeting.objects.all()


class PersonPaginationList(ListAPIView):
    """
    Person's list with pagination
    """

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class MeetingByPersonJob(ListAPIView):
    serializer_class = CountMeetingSerializer

    def get_queryset(self):
        return Meeting.objects.quantity_meetings_job()
