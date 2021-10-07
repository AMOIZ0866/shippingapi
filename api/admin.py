from django.contrib import admin

# Register your models here.
from api.models import PhoneOTP, User, Pickups, Dispatches, Deliveries

admin.site.register(PhoneOTP)
admin.site.register(User)
admin.site.register(Pickups)
admin.site.register(Dispatches)
admin.site.register(Deliveries)
