from django.db import models

from django.db.models import Q


class AuthorManager(models.Manager):
    """Managers for Author model"""

    def list_authors(self):

        return self.all()

    def find_author(self, kword):

        result = self.filter(name__icontains=kword)

        return result

    def find_author_or(self, kword):

        result = self.filter(Q(name__icontains=kword) | Q(last_name__icontains=kword))

        return result

    def find_author_exclude(self, kword):

        result = self.filter(name__icontains=kword).exclude(
            Q(age__icontains=44) | Q(age__icontains=56)
        )

        return result

    def find_author_gt(self, kword):

        result = self.filter(age__gt=40, age__lt=65).order_by('last_name', 'name')

        return result
