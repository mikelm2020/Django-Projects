from django.db import models
#
from django.db.models import Count


class MeetingManager(models.Manager):

    def quantity_meetings_job(self):
        result = self.values('person__job').annotate(
            quantity= Count('id')
        )
        print('*' * 20)
        print(result)
        return result
