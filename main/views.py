from django.shortcuts import render
from .models import Houses, Features, Amenity


# Create your views here.
def home(response):
    return render(response, "main/index.html")


def about(response):
    return render(response, "main/about.html", {})


def properties(response):
    myhouses = Houses.objects.all().values()
    return render(response, "main/property-grid.html", {"myhouses": myhouses})


def contact(response):
    return render(response, "main/contact.html", {})


def property_details(response, id):
    myhouses = Houses.objects.get(id=id)
    features = Features.objects.filter(house=myhouses)
    amenities = Amenity.objects.filter(features__in=features)
    return render(
        response,
        "main/property-single.html",
        {"myhouses": myhouses, "features": features, "amenities": amenities},
    )
