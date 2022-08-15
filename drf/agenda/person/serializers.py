from rest_framework import serializers, pagination
from .models import Person, Meeting, Hobby


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    active = serializers.BooleanField(required=False)


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = "__all__"


class PersonSerializer2(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            "id",
            "full_name",
            "job",
            "email",
            "phone",
            "hobbies",
        )


class MeetingSerializer(serializers.ModelSerializer):
    date_time = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = (
            "id",
            "date",
            "hour",
            "topic",
            "person",
            "date_time",
        )

    def get_date_time(self, obj):
        return str(obj.date) + " - " + str(obj.hour)


class MeetingSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            "id",
            "date",
            "hour",
            "topic",
            "person",
        )
        extra_kwargs = {
            "person": {"view_name": "person_app:detail", "lookup_field": "pk"}
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


class CountMeetingSerializer(serializers.Serializer):
    person__job = serializers.CharField()
    quantity = serializers.IntegerField()
