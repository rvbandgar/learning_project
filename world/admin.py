from django.contrib import admin

from .models import User, Country, City, Countrylanguage

admin.site.register(User)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Countrylanguage)


class CountryAdmin:
    list_display = ("code", "name", "continent")
    list_per_page = 10


class UserAdmin:
    list_display = ("first_name", "last_name", "username")
    list_per_page = 15
    exclude = ("phone_number",)
