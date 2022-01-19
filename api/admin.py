from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.
admin.site.register(CustomUser)
# admin.site.register(Role)
admin.site.register(Business)
# admin.site.register(UserRoles)
# admin,site.register(RolePermissions)
# admin.site.register(Desingation)
admin.site.register(Appointments)
admin.site.register(TimeSlots)
admin.site.register(reports)
admin.site.register(Feedback)
