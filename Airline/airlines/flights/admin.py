from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAmin(admin.ModelAdmin):
    list_display=(
        "id",
        "origin",
        "destination",
        "duration",
    )

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights", )

admin.site.register(Flight, FlightAmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)

