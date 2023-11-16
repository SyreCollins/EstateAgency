from django.contrib import admin
from .models import Houses, Features, Amenity

# Register your models here.

admin.site.register(Houses)
admin.site.register(Features)
admin.site.register(Amenity)
