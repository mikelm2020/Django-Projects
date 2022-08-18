from django.db import models


class ProductManager(models.Manager):
    def products_by_user(self, user):
        return self.filter(user_created=user)

    def products_with_stock(self):

        return self.filter(
            stok__gt=0,
        ).order_by("-num_sales")

    def products_by_gender(self, gender):
        if gender == "f":
            female = True
            male = False
        elif gender == "m":
            female = False
            male = True
        else:
            female = True
            male = True

        return self.filter(woman=female, man=male).order_by("created")

    def filter_products(self, **filters):
        return self.filter(
            man=filters["man"], woman=filters["woman"], name__icontains=filters["name"]
        )
