from django.db import models


class Houses(models.Model):
    RENT = "RENT"
    SALES = "SALES"
    TAG_CHOICES = [
        (RENT, "Rent"),
        (SALES, "Sales"),
    ]
    house_img = models.ImageField(upload_to="templates/main/img/")
    state = models.CharField(max_length=140)
    tag = models.CharField(
        max_length=5,
        choices=TAG_CHOICES,
        default=RENT,
    )
    area = models.FloatField(default=20)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    garages = models.IntegerField(default=0)
    # address = models.CharField(max_length=300)

    def __str__(self):
        return "House" + str(self.id)


class Amenity(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Features(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE)
    description = models.CharField(max_length=700, null=True)
    price = models.IntegerField()
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return "Features" + str(self.id)
