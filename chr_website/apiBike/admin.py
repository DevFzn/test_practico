from django.contrib import admin
from .models import Network, Location, Station, Extra

admin.site.register(Network)
admin.site.register(Location)
admin.site.register(Station)
admin.site.register(Extra)
